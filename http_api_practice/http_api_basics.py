import requests

# 基础语法
headers = {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}
params = {'page': 2, 'limit': 10}
data = {'username': 'alice', 'password': '123456'}
response_get = requests.get('https://api.github.com/user', headers=headers, params=params, timeout=5)
response_post = requests.post('https://api.example.com/users', headers=headers, data=data, timeout=5)

# 异常处理
try:
    response_get = requests.get('https://api.example.com/slow', timeout=5)
    response_get.raise_for_status() # 非2xx，报错HTTPError
    if response_get.status_code == 200:
        res = response_get.json()
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.ConnectionError:
    print("网络连接错误")
except requests.exceptions.HTTPError as err:
    print(f"HTTP 错误：{err}")