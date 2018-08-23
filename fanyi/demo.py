#/usr/bin/env python
#coding=utf-8
#本py封装为一个翻译器，
#

from hashlib import md5
from urllib  import request,parse
import random,json

rawtext=input('你想翻译什么') #输入


def createfanyi_url (rawtext,fromLang='en',toLang='zh'):
    appid = '20180822000197510' #你的appid
    secretKey = 'RX0ort_3oo5KZgF9LL39' #你的密钥
    sign1 = md5()
    salt = random.randint(32768, 65536)
    sign3=appid+rawtext+str(salt)+secretKey
    sign1.update(sign3.encode('utf-8'))
    sign2= sign1.hexdigest()
    fanyi_url='http://api.fanyi.baidu.com/api/trans/vip/translate' +'?appid='+appid+'&q='+parse.quote(rawtext)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign2
  
    try:
        with request.urlopen(fanyi_url) as f:
            content = json.loads(f.read())
            print(content['trans_result'][0]['dst'] )
    except Exception as  e:
        print (e)   
    finally:
        if httpClient:
            httpClient.close()
