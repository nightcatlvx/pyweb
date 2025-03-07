from src.common.repository.kafka.producer import KafkaProducerRepository
from src.common.constants import KafkaTopics  # 新增常量导入
from src.common.constants import MessageTypes  # 新增类型常量导入


class MessageService:
    def __init__(self, producer: KafkaProducerRepository):
        self.producer = producer

    async def send_alert(self, alert_data: dict):
        await self.producer.produce(
            topic=KafkaTopics.T_PYWEB_TEST,
            message_type=MessageTypes.SYSTEM_ERROR,
            data=alert_data,
        )
