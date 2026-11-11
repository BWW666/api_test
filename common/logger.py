import logging
import os

def get_logger():
    #创建日志对象
    logger = logging.getLogger("api_test")
    logger.setLevel(logging.INFO)

    #避免重复添加handler
    if not logger.handlers:
        #输出到控制台
        console_handler =logging.StreamHandler()
        #输出到文件
        file_handler = logging.FileHandler("run.log", encoding="utf-8")

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger
logger = get_logger()
