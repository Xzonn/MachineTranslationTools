from config import ExampleConfig, init_logger

from xzonn_mt_tools import update_mt_database

config = ExampleConfig(init_logger("更新数据库"))
update_mt_database(config)
