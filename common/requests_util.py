#common/requests_util.py
import requests
from config.settings import BASE_URL, TIMEOUT
from common.logger import logger

def send_request(method,url,**kwargs):
    """
    封装统一的请求方法
    :param method: 请求方法，如 GET, POST
    :param url: 接口路径
    :param kwargs: 其他参数，如 json, headers
    """
    full_url = BASE_URL + url if not url.startswith("http") else url
    logger.info(f"开始发送请求: [{method}] {full_url}")
    if "json" in kwargs:
        logger.info(f"请求参数：{kwargs['json']}")
    
    try:
        #调用requests库发送请求
        response = requests.request(method=method,url=full_url,timeout=TIMEOUT,**kwargs)
        logger.info(f"相应状态码：{response.status_code}")
        logger.info(f"响应内容：{response.text}")
        return response
    except requests.RequestException as e:
        logger.error(f"请求发生异常：{e}")
        raise e    