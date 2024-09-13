import logging
import os

from xzonn_mt_tools.config import Config


class ExampleConfig(Config):
  chinese_replace_dict = {
    "小叮当|机器猫|[多哆]啦[aＡａ○小]*[梦美]*": "哆啦A梦",
  }


def init_logger(file_name: str, stdout: bool = True) -> logging.Logger:
  os.chdir(os.path.dirname(__file__))
  os.makedirs("workspace", exist_ok=True)

  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

  fh = logging.FileHandler(f"workspace/{file_name}.log", "w", "utf8")
  fh.setFormatter(formatter)
  logger.addHandler(fh)

  if stdout:
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

  return logger
