import re
import urllib.request
import urllib
from collections import deque
#定义一些变量
queue = deque(' ') #将要爬的网址序列的编号
visited = set() #已爬取的合集

url_1 = 'http://www.heibanke.com/lesson/crawler_ex00/'  # 入口页面
url = url_1+queue[0]
#print(url) #test

while queue:
    the_num = queue.popleft()
    #print(the_num) #test
    the_url = url_1+the_num
    print(the_url)
    data = urllib.request.urlopen(the_url).read()
    data= data.decode('utf-8')
    #print(data)
    linkre = re.compile('\d{5}') #正则表达式
    print(linkre.findall(data))
    x = linkre.findall(data)[1]
    print(x)
    queue.append(x)