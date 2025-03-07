from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    async def connect(self):
        """初始化连接"""
        pass

    @abstractmethod
    async def disconnect(self):
        """关闭连接"""
        pass
