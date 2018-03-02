# coding=utf-8
__author__ = 'jql'

import re
import urllib
import os

# 初始化配置参数
number = 10  # 图片收集数量
path = 'img/'  # 图片存放目录


# 显示下载进度
def schedule(a, b, c):
    '''''
	a:已经下载的数据块
	b:数据块的大小
	c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

# 文件操作
if not os.path.exists(path):
    os.makedirs(path)


# 图片保存
def save_img(url, path, x):
    # print(url)
    message = None
    # try:
    # file = open(path + os.path.basename(url), 'wb')
    # request = urllib.request.urlopen(url)
    # file.write(request.read())

    target = path + '\\%s.jpg' % x
    print 'Downloading image to location: ' + target + '\nurl=' + url
    urllib.urlretrieve(url, target, schedule)

    # except Exception as e:
    #     message = str(e)
    # else:
    #     message = os.path.basename(url)
    # finally:
    #     if not file.closed:
    #         file.close()
    #     return message


'''
    获取整个页面内容
'''


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    # reg = r'src="(.+?\.jpg)" pic_ext'
    reg =r'src="(.+?\.jpg)" title'
    imgre = re.compile(reg)
    # imglist = imgre.findall(html)
    imglist = re.findall(imgre, html)

    x = 0
    for imgurl in imglist:
        # newImgUrl= imgurl.replace('src="', "").replace('"',"")
        # urllib.urlretrieve(imgurl,'%s.jpg' % x)
        save_img(imgurl, path, x)
        x += 1
    return imglist


urlString = "http://tieba.baidu.com/p/2460150866"
urlString1 = "http://image.baidu.com/"
urlString2 = "http://desk.zol.com.cn/meinv/"
html = getHtml(urlString2)

# print html
print getImg(html)
