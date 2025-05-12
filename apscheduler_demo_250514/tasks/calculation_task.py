from apscheduler_demo_250514.base.task import BaseTask


class CalculationTask(BaseTask):
    """계산 태스크"""

    def __init__(self, name: str, interval: int):
        super().__init__(name, interval)
        self.counter = 0

    def execute(self):
        self.counter += 1
        result = self.counter ** 2
        self.log(f"Calculation result: {self.counter}^2 = {result}")