from .base import BaseMessageHandler
from src.common.models.kafka import KafkaMessage
from src.common.constants import MessageTypes


class SendMessageHandler(BaseMessageHandler):
    @classmethod
    def can_handle(cls, message: KafkaMessage) -> bool:
        return message.type == MessageTypes.SEND_MESSAGE

    async def execute(self, data: dict) -> bool:
        # 实现具体业务逻辑
        print(f"处理SendMessage: {data}")
        return True
