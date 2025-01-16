import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

log_filename = datetime.now().strftime("logs/%Y%m%d_%H%M%S.log")

# ログの基本設定
logging.basicConfig(
    level=logging.DEBUG,  # ログレベル
    format='%(asctime)s - %(levelname)s - %(message)s',  # ログのフォーマット
    handlers=[
        logging.FileHandler(log_filename),  # logsディレクトリにxxx.logとして保存
        logging.StreamHandler()  # コンソールにも表示
    ],
    encoding='utf-8'

)

def get_logger():
    return logging.getLogger()

# # ログの使用例
# logging.debug("これはデバッグ用のログです")
# logging.info("これは情報のログです")
# logging.warning("これは警告のログです")
# logging.error("これはエラーのログです")
# logging.critical("これは致命的なエラーログです")