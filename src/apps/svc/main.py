from src.common.config import load_config
from src.common.repository.kafka.consumer import KafkaConsumerRepository


async def start_consumer():
    config = load_config(app_name="svc")  # 添加应用名称参数
    consumer = KafkaConsumerRepository(
        {
            "bootstrap_servers": config.bootstrap_servers,
            "group_id": config.consumer_group,
            "topic": config.producer_topics[0],
        }
    )

    await consumer.connect()
    # async for message in consumer.consume():
    #     # 处理消息逻辑
    #     process_message(message)


if __name__ == "__main__":
    start_consumer()
