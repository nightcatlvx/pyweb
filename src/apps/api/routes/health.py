from fastapi import APIRouter, Depends
from src.common.repository.kafka.producer import KafkaProducerRepository
# 修正导入路径和方式
from src.apps.api.di import get_kafka_producer

router = APIRouter()

@router.get("/health")
async def health_check(
    # 使用新的依赖注入方式
    producer: KafkaProducerRepository = Depends(get_kafka_producer)
):
    try:
        # 直接使用连接状态检查方法
        connected = await producer.check_connection()
        # 添加成功日志
        print(f"Kafka连接状态: {'已连接' if connected else '未连接'}") 
    except Exception as e:
        # 使用标准错误输出
        import traceback
        print(f"Kafka连接异常: {str(e)}\n{traceback.format_exc()}", flush=True)
        connected = False
        
    return {
        "status": "ok" if connected else "degraded",
        "kafka_status": "connected" if connected else "disconnected"
    }
