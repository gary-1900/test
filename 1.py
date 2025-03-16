import requests

# 抓取 x.com 首页信息
def fetch_x_com():
    url = 'https://x.com'
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    print(fetch_x_com())