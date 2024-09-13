from config import ExampleConfig, init_logger

from xzonn_mt_tools import compare_mt

config = ExampleConfig(init_logger("对比机翻", False))
compare_mt(config)
