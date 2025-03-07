from kafka import KafkaConsumer
import json
from src.common.models.kafka import KafkaMessage
from src.apps.svc.handlers import HANDLERS
from ..base_repo import BaseRepository


class KafkaConsumerRepository(BaseRepository):
    def __init__(self, config: dict):
        self.consumer = None
        self.config = config

    async def connect(self):
        self.consumer = KafkaConsumer(
            *self.config["consumer_topics"],
            bootstrap_servers=self.config["bootstrap_servers"],
            group_id=self.config["group_id"],
            auto_offset_reset="earliest",
            value_deserializer=lambda x: json.loads(
                x.decode("utf-8")
            ),  # 使用 json 模块
        )

    async def consume(self, topics: list[str]):
        async for msg in self._message_generator(topics):
            message = KafkaMessage.model_validate_json(msg.value)

            # 查找匹配的处理器
            for handler_cls in HANDLERS:
                if handler_cls.can_handle(message):
                    handler = handler_cls()
                    await handler.execute(message.data)
                    break
            else:
                print(f"未找到 {message.type} 的处理器")

    async def disconnect(self):
        if self.consumer:
            self.consumer.close()
