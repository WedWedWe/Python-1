import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    pass

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    head = html.find('img src=')
    while head != -1:
        tail = html.find('.jpg',head,head+255)
        if tail != -1:
            img_addrs.append('http:'+html[head+9:tail+4])
        else:
            tail = head+9
        head = html.find('img src=',tail)
    return img_addrs 

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
        

def download_mm(folder='Get_Pic',pages=70):
    os.mkdir(folder)
    os.chdir(folder)

    url ="http://jandan.net/ooxx/"
    
    for p1_ascii in range(65,90,4):
        p1 = chr(p1_ascii)
        for p2_num in range(0,2):
            p2 = str(p2_num)
            page_url = url + 'MjAyMDAxMzEtMT' + p1 + p2 +'#comments'
            img_addrs = find_imgs(page_url)
            save_imgs(folder, img_addrs)
                          
    for p1_ascii in range(65,90,4):
        p1 = chr(p1_ascii)
        for p2_word in range(119,121):
            p2 = chr(p2_word)
            page_url = url + 'MjAyMDAxMzEtMT' + p1 + p2 +'#comments'
            img_addrs = find_imgs(page_url)
            save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
