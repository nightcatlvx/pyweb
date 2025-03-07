from abc import ABC, abstractmethod
from src.common.models.kafka import KafkaMessage


class BaseMessageHandler(ABC):
    @classmethod
    @abstractmethod
    def can_handle(cls, message: KafkaMessage) -> bool:
        """判断是否可处理该类型消息"""
        pass

    @abstractmethod
    async def execute(self, data: dict) -> bool:
        """执行处理逻辑"""
        pass
