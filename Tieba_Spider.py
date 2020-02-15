import urllib.request as ur
import re
import os

def open_url(url):
    req = ur.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')
    page = ur.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_img(html):
    os.mkdir("TestTieba")
    os.chdir("TestTieba")
    
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)
    for each in imglist:
        filename = each.split("/")[-1]
        ur.urlretrieve(each,filename,None)

if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/6468851993"
    get_img(open_url(url))
