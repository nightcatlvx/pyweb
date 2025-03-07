from kafka import KafkaProducer
import asyncio  # 新增导入
from ..base_repo import BaseRepository
from src.common.models.kafka import KafkaMessage


class KafkaProducerRepository(BaseRepository):
    def __init__(self, config: dict):
        self.producer = None
        self.config = config  # 确保正确接收字典参数
    
    async def connect(self):
        self.producer = KafkaProducer(
            bootstrap_servers=self.config["bootstrap_servers"],
            value_serializer=lambda v: str(v).encode("utf-8"),
        )
        print(f"已连接到Kafka服务器: {self.config['bootstrap_servers']}", flush=True)
        self._connected = True  # 添加连接成功标记
    
    async def check_connection(self) -> bool:
        """检查Kafka连接状态"""
        try:
            if not self.producer:
                await self.connect()
    
            # 修改为同步等待方式
            future = self.producer.send('health-check', value=b'ping')
            # 使用事件循环包装同步等待
            connected = await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: future.get(timeout=5)
            )
            return bool(connected)
        except asyncio.TimeoutError:
            print("Kafka连接超时: 5秒内未收到响应", flush=True)
            return False
        except Exception as e:
            print(f"Kafka连接异常: {str(e)}", flush=True)
            return False
    
    async def disconnect(self):
        if self.producer:
            self.producer.close()
        self._connected = False  # 添加断开连接标记