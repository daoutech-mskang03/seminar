import asyncio
from apscheduler_demo_250514.base.task import BaseTask


class ImageAnalysisTask(BaseTask):
    """이미지 분석 태스크 (비동기)"""

    async def execute(self):
        self.log("이미지 분석 태스크 시작")

        # 이미지 로딩 시뮬레이션
        self.log("이미지 로드 중...")
        await asyncio.sleep(0.5)

        # LLM API 호출 시뮬레이션
        self.log("LLM API 호출 중...")
        await asyncio.sleep(0.5)

        # 응답 결과 처리 시뮬레이션
        detected_objects = ["person", "cat", "desk"]
        self.log(f"이미지 분석 결과: {', '.join(detected_objects)}")

        self.log("이미지 분석 태스크 완료")