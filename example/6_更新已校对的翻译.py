from config import ExampleConfig, init_logger

from xzonn_mt_tools import update_checked_mt

config = ExampleConfig(init_logger("更新已校对的翻译"))
update_checked_mt(config)
