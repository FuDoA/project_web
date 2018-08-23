from django.shortcuts import render
from hashlib import md5
from urllib  import request,parse
import random,json
# Create your views here.

def createfanyi (rawtext,fromLang='en',toLang='zh'):
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
            return content['trans_result'][0]['dst'] 
    except Exception as  e:
        print (e)   
    '''finally:
        if httpClient:
            httpClient.close()'''
            
            
def index (request):
    rg=request.GET
    if  'raw_text' in rg.keys():
        text1=request.GET['raw_text']
        transed_text=createfanyi(text1)
        return render(request,'fanyi/fanyi.html',{transed_text:transed_text})
    else  :
        return render(request,'fanyi/fanyi.html')