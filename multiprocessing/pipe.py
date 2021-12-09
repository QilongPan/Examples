"""
子进程调用parent_remote.close不会影响主进程的，主进程的依然未关闭,应该是创建子进程时重新深拷贝了
fork:https://blog.csdn.net/xy010902100449/article/details/44851453
https://blog.csdn.net/xy010902100449/article/details/44851453
"""
import time
from multiprocessing import Pipe
from multiprocessing.context import Process


def worker(parent_remote, child_remote, values):
    parent_remote.close()
    while True:
        values.append(1)
        print(child_remote.recv())
        time.sleep(18000)
        child_remote.send([2, "world", None])
        print(values)


parent_remote, child_remote = Pipe()
values = []
args = (parent_remote, child_remote, values)
process = Process(target=worker, args=args, daemon=True)
process.start()
child_remote.close()
while True:
    parent_remote.send([1, "hello", None])
    print(parent_remote.recv())
    values.append(2)
    print(values)
