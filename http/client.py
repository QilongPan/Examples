# demo_requests.py

import time

import requests

start_time = time.time()
response = requests.request("GET", "http://127.0.0.1:9999/")
print(f"need time {time.time() - start_time}")
print(response.status_code)  # 响应状态码
print("--------------------")
print(response.headers)  # 响应头
print("--------------------")
print(response.text)  # 响应体
