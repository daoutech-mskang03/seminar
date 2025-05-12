from typing import Dict, Type

from apscheduler_demo_250514.base.scheduler import BaseScheduler
from apscheduler_demo_250514.schedulers.background_scheduler import MyBackgroundScheduler
from apscheduler_demo_250514.schedulers.async_scheduler import MyAsyncScheduler
from apscheduler_demo_250514.schedulers.process_scheduler import MyProcessScheduler


class SchedulerFactory:
    """스케줄러 팩토리 클래스"""

    # 지원하는 스케줄러 타입과 클래스 매핑
    _schedulers: Dict[str, Type[BaseScheduler]] = {
        'background': MyBackgroundScheduler,
        'async': MyAsyncScheduler,
        'process': MyProcessScheduler
    }

    @classmethod
    def create_scheduler(cls, scheduler_type: str, name: str) -> BaseScheduler:
        """스케줄러 생성 메서드"""
        scheduler_class = cls._schedulers.get(scheduler_type)
        if not scheduler_class:
            raise ValueError(f"지원하지 않는 스케줄러 타입입니다: {scheduler_type}")

        scheduler = scheduler_class(name)
        scheduler.create_scheduler()
        return scheduler

    @classmethod
    def register_scheduler(cls, scheduler_type: str, scheduler_class: Type[BaseScheduler]):
        """스케줄러 등록 메서드"""
        cls._schedulers[scheduler_type] = scheduler_class
