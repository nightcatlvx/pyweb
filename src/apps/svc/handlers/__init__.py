import pkgutil
import importlib
from .base import BaseMessageHandler  # 新增基类导入

HANDLERS = []

for _, name, _ in pkgutil.iter_modules(__path__):
    if name != "base":
        module = importlib.import_module(f".{name}", __package__)
        # 改进点：使用 vars() 替代 dir() 获取模块真实属性
        for cls_name in vars(module):
            cls = getattr(module, cls_name)
            if (
                isinstance(cls, type)
                and issubclass(cls, BaseMessageHandler)
                and cls.__module__ == module.__name__  # 确保是模块内定义的类
            ):
                HANDLERS.append(cls)
