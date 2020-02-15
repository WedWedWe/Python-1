import urllib.request

url = 'http://45.32.164.128/ip.php'

proxy_support = urllib.request.ProxyHandler({'http':'198.98.55.168:8080'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
