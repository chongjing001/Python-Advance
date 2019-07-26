from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import hashlib

from utils import receive, reply,reply_help


def init_connet(request):
    if request.method == 'GET':
        try:
            if len(request.GET) == 0:
                return "hello, this is handle view"
            token = 'hello123'
            signature = request.GET.get('signature', '')
            timestamp = request.GET.get('timestamp', '')
            nonce = request.GET.get('nonce', '')
            echostr = request.GET.get('echostr', '')
            s = [timestamp, nonce, token]
            s.sort()
            s = ''.join(s)
            sha1 = hashlib.sha1(s.encode('utf-8'))
            # map(sha1.update, s)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                print('====验证通过====')
                return HttpResponse(echostr)
            else:
                print('====验证失败====')
                return ""
        except Exception as e:
            print('===error===', e)
            return e
    if request.method == 'POST':
        # print(request.body.decode())
        webData = request.body
        print('这是接收的xml: ',webData)
        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = recMsg.Content.decode('utf8')
            print(f'收到用户[{fromUser}]的消息：{content}')
            try:
                content = reply_help.qyk_reply(recMsg.Content)
                # content = reply_help.tx_reply(content)
            except Exception as e:
                print(e)
            print(f'机器人回的消息：{content}')
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            return HttpResponse(replyMsg.send())

        else:
            print("暂且不处理")
            return HttpResponse('')

