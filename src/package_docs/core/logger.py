import logging
from logging import Logger


def get_logger(name: str) -> Logger:
    """logger 반환.

    Args:
        name (str): logger 이름

    Raises:
        TypeError: name이 문자열이 아닐 경우 발생

    Returns:
        Logger: logger 객체
    """
    if not isinstance(name, str):
        raise TypeError("name은 반드시 문자열이어야 합니다.")
    
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger