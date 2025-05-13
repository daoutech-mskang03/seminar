import time
import logging

from typing import Dict, Any, List
from datetime import datetime
from multiprocessing import Process
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler_demo_250514.base.scheduler import BaseScheduler


def scheduler_worker(name: str, task_configs: List[Dict[str, Any]]):
    """독립적인 워커 프로세스에서 실행될 함수"""
    scheduler = BackgroundScheduler()
    logger = logging.getLogger(f"ProcessSchedulerWorker.{name}")

    # 태스크 클래스들을 다시 임포트 (워커 프로세스에서 필요)
    from apscheduler_demo_250514.tasks.image_processing_task import ImageProcessingTask

    # 태스크 생성 및 추가
    for task_config in task_configs:
        # 태스크 타입에 따라 적절한 클래스 생성
        if task_config['type'] == 'ImageProcessingTask':
            task = ImageProcessingTask(task_config['name'], task_config['interval'])
        # 다른 태스크 타입들 추가 가능...

        scheduler.add_job(
            task.execute,
            'interval',
            seconds=task.interval,
            id=task.name,
            name=task.name,
            next_run_time=datetime.now()
        )
        logger.info(f"태스크 [{task.name}]가 추가되었습니다.")

    # 스케줄러 시작
    scheduler.start()
    logger.info(f"스케줄러 [{name}]가 시작되었습니다.")

    try:
        # 메인 프로세스가 종료 신호를 보낼 때까지 실행
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        scheduler.shutdown()
        logger.info(f"스케줄러 [{name}]가 종료되었습니다.")


class MyProcessScheduler(BaseScheduler):
    def __init__(self, name: str):
        super().__init__(name)
        self.process = None
        self.task_configs = []  # 태스크 설정만 저장

    def create_scheduler(self):
        # 실제 스케줄러는 워커 프로세스에서 생성되므로 여기서는 아무 작업 안 함
        self.log("Process Scheduler가 생성되었습니다.")

    def add_task(self, task):
        self.tasks.append(task)  # BaseScheduler의 tasks 리스트에도 추가

        # 태스크 설정을 직렬화 가능한 형태로 저장
        task_config = {
            'type': task.__class__.__name__,
            'name': task.name,
            'interval': task.interval
        }
        self.task_configs.append(task_config)
        self.log(f"태스크 [{task.name}]가 Process Scheduler에 추가되었습니다.")

    def start(self):
        # 워커 프로세스 시작
        self.process = Process(
            target=scheduler_worker,
            args=(self.name, self.task_configs)
        )
        self.process.start()
        self.log("Process Scheduler가 시작되었습니다.")

    def shutdown(self):
        if self.process and self.process.is_alive():
            self.process.terminate()
            self.process.join()
        self.log("Process Scheduler가 종료되었습니다.")

    def get_jobs(self):
        return self.tasks
