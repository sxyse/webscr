# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import os

def main():
    result_root_path = 'mm36dpic/'  # 图片保存目录
    request_root_url = 'http://mm36d.com/belle/1/1/'  # 根URL
    request_param_1 = 0  # 参数1
    total_image_count = 0  # 图片递增总数

    # 创建文件夹
    if not os.path.exists(result_root_path):
        os.makedirs(result_root_path)

    while True:
        if request_param_1 > 5:
            break
        request_param_1 += 1  # 参数1加1
        request_param_2 = 0  # 参数2

        # 请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5 ',
            'Accept': 'text/plain',
            'Connection': 'close'
        }

        while True:
            request_param_2 += 1  # 参数2加1
            request_url = request_root_url + str(request_param_1) + '/' + str(request_param_2)  # 拼接URL

            print('Page: ' + request_url)

            requests.session().keep_alive = False

            try:
                # 获取页面内容
                response = requests.get(request_url, headers=headers, allow_redirects=False)

                # 请求成功
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')  # BeautifulSoup解析
                    response.close()  # 关闭请求
                    image_url = soup.find('img', {'class': 'lazy'})['data-original']  # 提取图片URL

                    response = requests.get(image_url)  # 下载图片
                    image_file = open(result_root_path + str(total_image_count) + '.jpg', 'wb')  # 创建图片文件
                    image_file.write(response.content)  # 写图片
                    image_file.close()  # 关闭文件
                    response.close()  # 关闭请求

                    total_image_count += 1  # 计数增加
                    print(image_url + ' done. Current: ' + str(total_image_count))
                else:
                    print('Next page')
                    break
            except Exception as e:
                print('Error: ' + e.__doc__)


if __name__ == '__main__':
    main()