#!/usr/bin/env python
# encoding: utf-8

import urllib
import urllib2
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

print '#'*50
print '本程序主要采集豆瓣小组的图片'
print '#'*50

print '采集前输入代理服务器地址，这样可以防止被豆瓣屏蔽'
print '推荐一个代理地址：http://cn-proxy.com'
print '之需要输入服务器地址以及端口好，不需要输入http'
print '例子:127.0.0.1:8080'

print '#'*50
proxy_input=raw_input('请输入采集代理服务器:')
proxy_handler=urllib2.ProxyHandler({'http':'%s' %proxy_input})
opener=urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

#采集本地路径全局变量
#img_LuJ=raw_input("路径：")
#~/doban
#设置UserAgent
#req=urllib2.Request(HuoQ)
#req.add_header('User-Agent','Mozilla/5.0(X11;Linux i686) AppleWebKit/537.36 (KHTML,like Gecko)Chrom/35.0.1916.153 Safari/537.36')
#reader=urllib2.urlopen(req)

#print reader.read()

#获取帖子单页html
def gethtml2(url2):
    html2=urllib2.urlopen(url2).read().decode('utf-8')
    return html2
#抽取图片并下载列表
def gettoimg(html2):
    req2=r'http://www.douban.com/group/topic/\d+'
    toplist=re.findall(reg2,html2)
    x=0
    #限制下载图片数量
    #输出topicurl 每次输出一个循环
    for topicurl in toplist:
        x+=1
    return topicurl
#下载图片到本地
def download(topic_page):
    reg3=r'http://img3.douban.com/view/group_topic/large/public/.|\.jpg'
    imglist=re.findall(reg3,topic_page)
    i=1
    download_img=None
    for imgurl in imglist:
        img_numlist=re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            download_img=urllib.urlretrieve(imgurl,'~/%s.jpg'%img_num)
            time.sleep(1)
            i+=1
            print (imgurl)
    return download_img

page_end=int(input('请输入采集页码数:'))
num_end=page_end*25
num=0
page_num=1
while num<=num_end:
    html2=gethtml2('http://www.douban.com/group/haixiuzu/discussion?start=%d'%num)
    #抽取下载图片
    topicurl=gettoimg(html2)
    topic_page=gethtml2(topicurl)
    download_img=download(topic_page)
    num=page_num*25
    page_num+=1
else:
    print '程序采集完成'
