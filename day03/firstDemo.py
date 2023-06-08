import os
import time
import urllib.request
import requests as req
# if not os.path.exists('lk'):
#     os.mkdir('lktest')
# if not os.path.exists('lktest/test.txt'):
#     file = open('lktest/test.txt','w')
#     file.write('测试成功')
#     file.close()
# print(os.getcwd());
# print(os.path);
# 获取两天前时间并且自定义的格式
# curtime = time.time()
# tooDay = curtime - 60*60*24*2
# print(time.strftime('%Y-%m-%d %H时%M分%S秒', time.localtime(tooDay)))

# response= urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# res = req.get('http://www.baidu.com')
# print
arr = [7,8,9]
n = range(len(arr))
for i in n:
    print(i)