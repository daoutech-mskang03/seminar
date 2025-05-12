import time

from datetime import datetime

from apscheduler_demo_250514.base.task import BaseTask


class ImageProcessingTask(BaseTask):
    """이미지 처리 태스크 (CPU 집약적)"""

    def execute(self):
        self.log("이미지 처리 태스크 시작")

        # 이미지 로딩 시뮬레이션
        self.log("이미지 파일 로드 중...")
        time.sleep(0.1)

        # 이미지 포맷 변환 시뮬레이션
        self.log("webp 파일로 변환 중...")
        time.sleep(0.2)

        # 이미지 크기 조정 시뮬레이션
        self.log("이미지 리사이즈 중...")
        time.sleep(0.3)

        # 이미지 인코딩 시뮬레이션
        self.log("Base64 인코딩 중...")
        time.sleep(0.2)

        # DB 저장 시뮬레이션
        self.log("DB에 처리 결과 저장 중...")
        time.sleep(0.1)

        self.log("이미지 처리 태스크 완료")