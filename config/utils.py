# utils.py
from typing import List, Dict
import os
import logging
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import json

class Logger:
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg: str):
        self.logger.info(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)

def load_json(file: str) -> Dict:
    with open(file, 'r') as f:
        return json.load(f)

def save_json(file: str, data: Dict):
    with open(file, 'w') as f:
        json.dump(data, f)

def get_env_var(var: str) -> str:
    return os.environ.get(var)

def get_timestamp() -> int:
    return int(datetime.now().timestamp())

def get_relative_delta(start: int, end: int) -> int:
    delta = timedelta(seconds=end - start)
    return delta.days * 24 * 60 * 60 + delta.seconds

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class AbstractBaseClass(ABC):
    @abstractmethod
    def method(self):
        pass