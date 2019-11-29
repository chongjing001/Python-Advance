
from common.functions import is_login

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from common.redis_handle import RedisHandle
# chat/views.py
from django.utils.safestring import mark_safe
import json


from user.models import User

hash_user = 'user'


def refresh_user_list(redis_conn):
    channel_layer = get_channel_layer()
    text = get_user_data(redis_conn)
    message = {
        "text": text,
        "sender_type": 3,  # 刷新数据标识
    }
    async_to_sync(channel_layer.group_send)("chat_%s" % "public_room",
                                            {"type": "chat_message", "message": message})


def get_user_data(r, username=None):
    all_users = r.hash_get_all_data(hash_user)
    text = []
    for (key, value) in all_users.items():
        if not username:
            text.append(json.loads(value))
        else:
            if key != username:
                text.append(json.loads(value))
    return text


@api_view(['GET'])
def init_ws_pubic_room(request):
    user_id = request.session['user_id']
    user = User.objects.filter(pk=user_id).first()
    username = user.username
    public_room = 'public_room'
    r = RedisHandle(db_sign='on_line')
    tmp = dict(id=user.id, name=username)
    r.hash_add_or_up_data(hash_user, username, json.dumps(tmp))
    refresh_user_list(r)
    on_line_user_list = get_user_data(r, username=username)
    r.close_connect()

    return JsonResponse({'code': 200, 'msg': 'success', 'username': username, 'public_room': public_room,
                         'on_line_user_list': on_line_user_list})


@api_view(['POST'])
def user_off_line(request):
    name = request.data.get('name','')
    r = RedisHandle(db_sign='on_line')
    r.hash_del_data(hash_user,name)
    refresh_user_list(r)
    r.close_connect()

    return JsonResponse({'code':200,'msg':'success'})




@is_login
def index(request):
    return render(request, 'chat/index.html')
