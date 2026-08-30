import logging

def _get_log_level():
    from utils.settings import LOG_LEVEL
    
    match LOG_LEVEL:
        case 'CRITICAL': 
            return 50
        case 'ERROR':
            return 40
        case 'WARNING':
            return 30
        case 'INFO':
            return 20
        case 'DEBUG':
            return 10
        case _:
            raise Exception('Invalid log level')

def _get_formatter():
    return logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s :: %(message)s")

def _create_console_handler():
    handler = logging.StreamHandler()
    handler.setLevel(_get_log_level())
    handler.setFormatter(_get_formatter())
    return handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(_get_log_level())
    logger.addHandler(_create_console_handler())
    return logger

