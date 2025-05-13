from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from apscheduler_demo_250514.base.scheduler import BaseScheduler


class MyAsyncScheduler(BaseScheduler):
    def create_scheduler(self):
        self.scheduler = AsyncIOScheduler()
        self.log("AsyncIOScheduler가 생성되었습니다.")

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
        self.log(f"태스크 [{task.name}]가 AsyncIOScheduler에 추가되었습니다.")

    def start(self):
        self.scheduler.start()
        self.log("AsyncIOScheduler가 시작되었습니다.")

    def shutdown(self):
        self.scheduler.shutdown()
        self.log("AsyncIOScheduler가 종료되었습니다.")

    def get_jobs(self):
        return self.tasks
