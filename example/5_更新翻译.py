from config import ExampleConfig, init_logger

from xzonn_mt_tools import update_translations

config = ExampleConfig(init_logger("更新翻译", False))
update_translations(config)
