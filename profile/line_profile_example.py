"""
lineprofiler github:https://github.com/pyutils/line_profiler
运行方式:
需要测试的函数需要加上装饰器@profile
step1: kernprof -l line_profile_example.py
step2: python -m line_profiler line_profile_example.py.lprof
"""


@profile
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [
    64,
    34,
    25,
    12,
    22,
    11,
    90,
    10,
    20,
    15,
    100,
    102,
    101,
    1000,
    2000,
    1996,
    1958,
]

bubbleSort(arr)
