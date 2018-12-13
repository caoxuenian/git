import urllib.request
import urllib.parse
import json
import time


while True:
    cotent = input("请输入要翻译的内容,q!退出：")
    if cotent == "q!":
        break
    if cotent =="":
        continue
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    head={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWeb"}


    data = {"i":cotent,"doctype":'json',"keyfrom": 'fanyi.web',"typoResult":'true'}
    data = urllib.parse.urlencode(data).encode('utf-8')

    rep = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(rep)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print("翻译结果：%s"%(target['translateResult'][0][0]['tgt']))
    time.sleep(3)
