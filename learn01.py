import urllib
import urllib.request

data ={}
data['word']= 'python scrapy'
url_values=urllib.parse.urlencode(data)
url= "http://www.baidu.com/s?"
full_url = url+url_values

data = urllib.request.urlopen(full_url).read()
data= data.decode('utf-8')
print(data)


########如何读取一个网址的内容#########