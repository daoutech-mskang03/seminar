import logging

from typing import Dict

from apscheduler_demo_250514.base.scheduler import BaseScheduler

logger = logging.getLogger(__name__)


class SchedulerRegistry:
    """스케줄러 레지스트리 클래스"""

    def __init__(self):
        self.schedulers: Dict[str, BaseScheduler] = {}

    def add_scheduler(self, name: str, scheduler: BaseScheduler):
        """스케줄러 추가 메서드"""
        self.schedulers[name] = scheduler
        logger.info(f"스케줄러 [{name}]가 등록 되었습니다.")

    def get_scheduler(self, name: str) -> BaseScheduler:
        """스케줄러 조회 메서드"""
        return self.schedulers.get(name)

    def start_all(self):
        """모든 스케줄러 시작 메서드"""
        for name, scheduler in self.schedulers.items():
            scheduler.start()
            # logger.info(f"스케줄러 [{name}]가 시작 되었습니다.")

    def stop_all(self):
        """모든 스케줄러 종료 메서드"""
        for name, scheduler in self.schedulers.items():
            scheduler.shutdown()
            # logger.info(f"스케줄러 [{name}]가 종료 되었습니다.")

    def list_schedulers(self):
        """등록된 스케줄러 목록 조회 메서드"""
        logger.info("등록된 스케줄러 목록:")
        for name, scheduler in self.schedulers.items():
            logger.info(f"* {name}: {scheduler.__class__.__name__}")
            for task in scheduler.get_jobs():
                logger.info(f"  - 태스크: {task.name}, 주기: {task.interval}초")