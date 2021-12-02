import cProfile

"""
https://docs.python.org/3/library/profile.html
由于输出可能会很长，可以通过>将输出写入文件
"""


def test():
    sum_num = 0
    for i in range(1000000):
        sum_num += i


# cProfile.run('re.compile("test")')
# test()
cProfile.run("test()")
