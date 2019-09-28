from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from common.redis_handle import RedisHandle
# chat/views.py
from django.utils.safestring import mark_safe
import json

# def index(request):
#     return render(request, 'chat/index.html', {})

# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })

hash_user = 'user'


def refresh_user_list(redis_conn, username):
    channel_layer = get_channel_layer()
    text = get_user_data(redis_conn, username)
    message = {
        "text": text,
        "sender_type": 3,  # 刷新数据标识
    }
    async_to_sync(channel_layer.group_send)("chat_%s" % 'customer_service',
                                            {"type": "chat.message", "message": message})


def get_user_data(r, username):
    all_users = r.hash_get_all_data(hash_user)
    text = []
    for (key, value) in all_users.items():
        if key != username:
            text.append(json.loads(value))
    return text


@api_view(['GET'])
def init_ws_pubic_room(request):
    user = request.user
    username = user.username
    public_room = 'public_room'
    r = RedisHandle(db_sign='on_line')
    tmp = dict(id=user.id, name=username)
    r.hash_add_or_up_data(hash_user, username, json.dumps(tmp))
    refresh_user_list(r, username)
    on_line_user_list = get_user_data(r, username)
    r.close_connect()

    return JsonResponse({'code': 200, 'msg': 'success', 'username': username, 'public_room': public_room,
                         'on_line_user_list': on_line_user_list})
