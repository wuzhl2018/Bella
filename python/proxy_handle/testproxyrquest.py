#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-04-28 11:54:05
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 测试利用requests模块添加代理访问网络

import requests

test_ip = '116.209.56.118'
test_port = '9999'

def test_proxy_request(ip, port):
    # 代理IP地址
    proxy_data = {
        'http': 'http://' + ip + ':' + port,
        'https': 'http://' + ip + ':' + port,
    }

    # 客户端说明
    head_data = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Connection': 'keep-alive'
    }

    try:
        # 该返回当前的IP地址，http://icanhazip.com提供返回当前外网IP的服务
        response = requests.get('http://icanhazip.com', headers=head_data, proxies=proxy_data)
        outer_ip = response.text.strip().replace('\n', '')
        return outer_ip == ip
    except:
        return False

if __name__ == '__main__':
    test_result = test_proxy_request(test_ip, test_port)
    if test_result:
        print("IP代理成功 ==> {0}:{1}".format(test_ip, test_port))
    else:
        print("IP代理失败 ==> {0}:{1}".format(test_ip, test_port))

'''
IP代理成功 ==> 116.209.56.118:9999
'''
