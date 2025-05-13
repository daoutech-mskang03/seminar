import logging

from abc import ABC, abstractmethod


class BaseScheduler(ABC):
    """스케줄러의 기본 클래스"""

    def __init__(self, name: str):
        """
        스케줄러의 기본 클래스 초기화

        Args:
            name (str): 스케줄러 이름
        """
        self.name = name
        self.scheduler = None
        self.logger = logging.getLogger(f"{self.__class__.__name__}.{name}")
        self.tasks = []

    @abstractmethod
    def create_scheduler(self):
        """스케줄러 인스턴스 생성"""
        pass

    @abstractmethod
    def add_task(self, task: 'BaseTask'):
        """태스크 추가"""
        pass

    @abstractmethod
    def start(self):
        """스케줄러 시작"""
        pass

    @abstractmethod
    def shutdown(self):
        """스케줄러 종료"""
        pass

    @abstractmethod
    def get_jobs(self):
        """스케줄러의 모든 작업 조회"""
        pass

    def log(self, message: str):
        """로그 출력"""
        self.logger.info(f"[{self.name}] {message}")
