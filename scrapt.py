import urllib.request
url = "http://www.heibanke.com/lesson/crawler_ex00/"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)