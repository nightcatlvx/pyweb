from typing import AsyncGenerator  # 修改导入类型
from fastapi import Depends
from src.common.repository.kafka.producer import KafkaProducerRepository
from src.common.config import load_config


# 修改返回类型为异步生成器
async def get_kafka_producer() -> AsyncGenerator[KafkaProducerRepository, None]:
    config = load_config(app_name="api")
    producer = KafkaProducerRepository(config.kafka.__dict__)
    await producer.connect()  # 添加显式连接
    yield producer
    await producer.disconnect()

# 修改返回类型为直接依赖
async def get_kafka_producer() -> KafkaProducerRepository:
    config = load_config(app_name="api")
    producer = KafkaProducerRepository({
        "bootstrap_servers": config.kafka.bootstrap_servers
    })
    await producer.connect()
    return producer
async def get_kafka_producer() -> AsyncGenerator[KafkaProducerRepository, None]:
    config = load_config(app_name="api")
    producer = KafkaProducerRepository({
        "bootstrap_servers": config.kafka.bootstrap_servers
    })
    await producer.connect()
    yield producer
    await producer.disconnect()

