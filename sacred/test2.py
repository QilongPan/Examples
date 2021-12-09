from sacred import Experiment

ex = Experiment()


@ex.main
def my_main():
    pass


if __name__ == "__main__":
    ex.run_commandline()

# 以上代码与下面等价
"""
from sacred import Experiment

ex = Experiment()


@ex.automain
def my_main():
    pass
"""
