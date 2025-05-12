import asyncio
import logging

from apscheduler_demo_250514.factory import SchedulerFactory
from apscheduler_demo_250514.registry import SchedulerRegistry

from apscheduler_demo_250514.tasks.simple_task import SimpleTask
from apscheduler_demo_250514.tasks.calculation_task import CalculationTask
from apscheduler_demo_250514.tasks.image_analysis_task import ImageAnalysisTask
from apscheduler_demo_250514.tasks.image_processing_task import ImageProcessingTask

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


async def main():
    logger.info("=== APScheduler 데모 시작 ===")

    # 스케줄러 레지스트리 생성
    registry = SchedulerRegistry()

    # 1. BackgroundScheduler 데모
    bg_scheduler = SchedulerFactory.create_scheduler('background', 'bg_demo')
    bg_scheduler.add_task(SimpleTask('간단한 태스크', 3))
    bg_scheduler.add_task(CalculationTask('계산 태스크', 5))
    registry.add_scheduler('background 데모', bg_scheduler)

    # 2. AsyncIOScheduler 데모 (이미지 분석)
    async_scheduler = SchedulerFactory.create_scheduler('async', 'async_demo')
    async_scheduler.add_task(ImageAnalysisTask('이미지 분석 태스크', 7))
    registry.add_scheduler('async 데모', async_scheduler)

    # 3. ProcessScheduler 데모 (이미지 처리)
    process_scheduler = SchedulerFactory.create_scheduler('process', 'process_demo')
    process_scheduler.add_task(ImageProcessingTask('이미지 처리 태스크', 9))
    registry.add_scheduler('process 데모', process_scheduler)

    # 모든 스케줄러 목록 출력
    registry.list_schedulers()

    # 모든 스케줄러 시작
    registry.start_all()

    try:
        logger.info("스케줄러가 실행 중입니다. Ctrl+C를 눌러 종료하세요.")
        await asyncio.sleep(60)

    except KeyboardInterrupt:
        logger.info("사용자에 의해 종료되었습니다.")

    finally:
        logger.info("모든 스케줄러를 종료합니다...")
        registry.stop_all()
        logger.info("=== APScheduler 데모 종료 ===")


if __name__ == "__main__":
    asyncio.run(main())
