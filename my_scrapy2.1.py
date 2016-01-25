
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
#解压函数
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data
#获取_xsrf    这个值虽然叫_xsrf,但是也有叫别的名字的，他的目的是为了防止CSRF跨站攻击，不同网站的值是不一样的，要注意。
def getXSRF(data):
    cer = re.compile('name=\'csrfmiddlewaretoken\' value=\'(.*)\'', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
#构造文件头    #这有待学习
def getOpener(head):   #有待加强了解
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.heibanke.com',
}

url = 'http://www.heibanke.com/lesson/crawler_ex01/ '
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)     # 解压
#print(data.decode('utf-8'))
_xsrf = getXSRF(data.decode())
#print(_xsrf)
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）

#对返回的网页抓取核心H3句子
def get_the_key(x):
    cer = re.compile('<h3>.+</h3>')
    strlist = cer.findall(x)
    return strlist[0]
#
for password in range(1,30):
    print('正在尝试密码为'+str(password)+'的登录')
    id = 'ls'

    #构造Post数据，他也是从抓大的包里分析得出的。

    postDict = {
        'csrfmiddlewaretoken':_xsrf, #特有数据，不同网站可能不同，这个题里面就是
        'username': id,
        'password': password,
       }
    #需要给Post数据编码
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(url, postData)
    op = opener.open(url, postData)
    m = op.read()
    m =ungzip(m).decode()
    print(get_the_key(m))
    if'密码错误' not in m:
        print(m)
        break
#
#op = opener.open(url, postData)
#m = op.read()
#m =ungzip(m).decode()
#if'密码错误' in m:
#    print('密码错误')
#    password =int(password)+1
#else:
#    print('未出现密码错误')
#    print(m)
#if'密码错误' in m:
