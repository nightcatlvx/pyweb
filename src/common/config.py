import os
from dotenv import load_dotenv
import json
from pathlib import Path
from pydantic import BaseModel


class Config:
    def __init__(self, data: dict):
        for k, v in data.items():
            setattr(self, k, v if not isinstance(v, dict) else Config(v))

class KafkaConfig(BaseModel):
    bootstrap_servers: str

def load_config(app_name: str):
    env = os.getenv("APP_ENV", "dev")
    # 修正后的路径计算逻辑
    config_path = (
        Path(
            __file__
        ).parent.parent  # 原先是 parent.parent.parent (到根目录)，改为到 src 目录
        / "apps"
        / app_name
        / "configs"
        / f"config.{env}.json"
    )

    with open(config_path, "r") as f:
        return Config(json.load(f))
