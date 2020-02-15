import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

while True:
    data={}
    head={}
    getstr = input('English:')
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    data['i'] = getstr
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15803894145095'
    data['sign'] = 'ed81f31b4b62d7f66611e49f6ecd684b'
    data['ts'] = '1580389414509'
    data['bv'] = '9915c65c9e78cfd742d6a24e66b85108'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    tgt = json.loads(html)
    print('Chinese:%s' % (tgt['translateResult'][0][0]['tgt']))

