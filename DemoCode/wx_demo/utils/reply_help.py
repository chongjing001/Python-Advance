import json
import random
import time
import urllib.request
import requests

def tl_reply(text_input):
    """
    图灵机器人api
    :param text_input:
    :return:
    """
    api_url = "http://openapi.tuling123.com/openapi/api/v2"

    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": text_input
                    },

                "selfInfo":
                    {
                        "location":
                            {
                                "city": "成都",
                                "province": "四川",
                                "street": "天府三街"
                            }
                    }
            },

        "userInfo":
            {
                "apiKey": "873f914b965c45edb799629fe32ed2c2",
                "userId": "OnlyUseAlphabet"
            }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('Turing的回答：')
    print('code：' + str(intent_code))
    print('text：' + results_text)
    return results_text


def qyk_reply(text_input):
    """
    青云客智能聊天机器人API
    :param text_input: 用户的问题
    :return: 机器人回答
    """
    api_url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={text_input}'
    http_post = urllib.request.Request(api_url, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(json.loads(response_str))
    # print(type(json.loads(response_str)))
    return json.loads(response_str)['content']


def tx_reply(text_input):
    """
    腾讯闲聊机器人api
    :param text_input:
    :return:
    """
    # 请求参数配置
    app_id = 2117545630
    time_stamp = time.time()
    nonce_str = 'ffd54f5' + str(random.randint(0, 5512))
    sign = 'abcd' * 8
    session = '10000'
    question = text_input

    api_url = f'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat?app_id={app_id}&time_stamp={time_stamp}&nonce_str={nonce_str}&sign={sign}&session={session}&question={question}'
    url = api_url

    response = requests.get(url)
    if response.status_code == 200:
        print(response.content.decode('utf-8'))
    print('*******************',response)

