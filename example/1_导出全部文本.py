from config import ExampleConfig, init_logger

from xzonn_mt_tools import export_all_lines

config = ExampleConfig(init_logger("导出全部文本"))
export_all_lines(config)
