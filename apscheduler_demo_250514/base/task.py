import logging

from abc import ABC, abstractmethod


class BaseTask(ABC):
    def __init__(self, name: str, interval: int):
        self.name = name
        self.interval = interval
        self.logger = logging.getLogger(f"Task.{name}")

    @abstractmethod
    def execute(self):
        """태스크 실행"""
        pass

    def log(self, message: str):
        """로그 출력"""
        self.logger.info(f"[{self.name}] {message}")