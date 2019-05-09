#### 话不多说，直接上代码
```python
# 导入requests库
import requests

# 需要转换的长链接
long_url = "https://github.com/chongjing001/MyProject/tree/master/renting"
querystring = {"url":long_url}

# 调用接口实现（感谢大神的接口）
url = "http://suo.im/api.php"

# 转换
response = requests.request("GET", url, params=querystring)

print(response.text)

>>>
http://suo.im/4APBBP
```

**--------------------------------------------分割线---------------------------------------------**
#### 下面说一下原理
- 1.长链接转换为短链接核心就是进制转换
- 2.十进制数转为62进制(  0~9 + 	A~Z  + a~z )共62个字符
- 3.假如允许转换的10进制数范围为 10 000 000~ 99 999 999 （唯一，相当于数据库主键）每一个数字对应一个长链接，再转为62进制数
- 4.浏览器解析时，现将短链接（62进制数）转换成 10进制数  --- > 再找到对应的长链接，最后解析

```python
# 数字转62进制
def convert(num):
    global all_chars
    all_chars = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    digits = []
    while num > 0:
    	# 拿到对应的下标取得62进制数，并插入列表0号位
        digits.insert(0, all_chars[num % 62])
        num//= 62
    return ''.join(digits)

# 例：12 000 000 转为62进制数为 oLkO
print(convert(12000000))
>>>>
'oLkO'
```