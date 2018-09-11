"""
    Author : YangBo
    Time : 2018-09-11 14:21
    function:利用爬虫技术爬取1号店网站，爬取有关裙子的尺寸进行分析.
"""
# 导入相关包
import time    # 让爬虫休眠
import os      # 存储爬取内容
from urllib.request import urlretrieve   # 下载图片
import requests     # 发起请求
from lxml import etree   # 图片导入筛选.

headers_base = {  # 字符串'User-Agent'为字典的key,其后为字典的元素.
    # 请求头:
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}


def download_page(page_url, save_path):
    response = requests.get(page_url, headers_base)
    print(response)     # 打印状态码.
    html = etree.HTML(response.text)    # 解析状态内容.
    print(html)
    img_url = html.xpath(".//div[@class='img-l-box']/div/img/@src")
    # iter__可以被迭代
    # '.// a[ @class ='img'] / div / img / @ src'
    num = 13
    for i in img_url:

        img = 'http:' + str(i)     # 拼接
        print(img)
        # 图片命名.
        name = os.path.join(save_path, str(num)+'.jpg')
        # 开始下载图片.
        urlretrieve(img, name)
        num += 1


save_path = 'D:\pycharm\code\Internet_worm\Internet_stom_image'
path_url = 'http://588ku.com/ycbeijing/5665827.html'
download_page(path_url, save_path)