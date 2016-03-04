__author__ = 'Ls'
# -*- coding:utf-8 -*-
import urllib,urllib.request,urllib.parse,re

url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%BC%96%E8%BE%91&p=1&isadv=0'

x= urllib.request.urlopen(url).read().decode('utf-8')
#print(x)

#利用正则表达式获取网址
def find_out(the_read_url):
    linkre = re.compile('"http://jobs.zhaopin.com/.\d*?.htm"')# 正则表达式，需要每次不同时候都调整
    x=linkre.findall(the_read_url)
    return x

print(find_out(x))