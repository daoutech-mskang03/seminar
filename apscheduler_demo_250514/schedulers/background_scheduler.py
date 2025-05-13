from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler_demo_250514.base.scheduler import BaseScheduler


class MyBackgroundScheduler(BaseScheduler):
    """백그라운드 스케줄러"""

    def create_scheduler(self):
        self.scheduler = BackgroundScheduler()
        self.log("BackgroundScheduler가 생성되었습니다.")

    def add_task(self, task):
        self.tasks.append(task)
        self.scheduler.add_job(
            task.execute,
            'interval',
            seconds=task.interval,
            id=task.name,
            name=task.name,
            next_run_time=datetime.now()
        )
        self.log(f"태스크 [{task.name}]가 BackgroundScheduler에 추가되었습니다.")

    def start(self):
        self.scheduler.start()
        self.log("BackgroundScheduler가 시작되었습니다.")

    def shutdown(self):
        self.scheduler.shutdown()
        self.log("BackgroundScheduler가 종료되었습니다.")

    def get_jobs(self):
        return self.tasks
