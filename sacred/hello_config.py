"""
tutorial:https://sacred.readthedocs.io/en/stable/configuration.html#defining-a-configuration
"""
from sacred import Experiment

ex = Experiment("hello_config")


@ex.config
def my_config():
    recipient = "world"
    message = "Hello %s!" % recipient


@ex.automain
def my_main(message):
    print(message)


"""
python hello_config.py
python hello_config.py print_config
python hello_config.py with recipient="that is cool"
"""

