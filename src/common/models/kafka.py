from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class KafkaMessage(BaseModel, Generic[T]):
    type: str  # 消息类型标识 (如 SendMessage)
    data: T  # 消息内容体
