from config import ExampleConfig, init_logger

from xzonn_mt_tools import split_texts

config = ExampleConfig(init_logger("分割文本"))
split_texts(config)
