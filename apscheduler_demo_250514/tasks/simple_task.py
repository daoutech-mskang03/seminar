from datetime import datetime

from apscheduler_demo_250514.base.task import BaseTask


class SimpleTask(BaseTask):
    """단순 태스크 예제"""
    def execute(self):
        self.log(f"SimpleTask executed at {datetime.now().strftime('%H:%M:%S')}")