from sacred import Experiment

ex = Experiment("config_demo")

# method1
@ex.config
def my_config():
    """This is my demo configuration"""

    a = 10  # some integer

    # a dictionary
    foo = {"a_squared": a ** 2, "bar": "my_string%d" % a}
    if a > 8:
        # cool: a dynamic entry
        e = a / 2


@ex.config
def my_config2(a):  # notice the parameter a here
    c = a * 2  # we can use a because we declared it
    a = -1  # we can also change the value of a
    # d = b + '2'    # error: no access to b


# method2
ex.add_config(d=10)

# method3
ex.add_config("config.json")


@ex.automain
def run():
    pass


"""
多个config配置时会按照顺序被执行
python test6.py print_config
可以输出配置的参数

生成File Observe
python test_config.py -F logs
"""
