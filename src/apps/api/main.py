from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.common.config import load_config
from src.common.repository.kafka.producer import KafkaProducerRepository

config = load_config(app_name="api")  # 添加应用名称参数


@asynccontextmanager
async def lifespan(app: FastAPI):
    global kafka_producer
    # 将vars(config.kafka)改为直接访问字典属性
    kafka_producer = KafkaProducerRepository({
        "bootstrap_servers": config.kafka.bootstrap_servers
    })
    await kafka_producer.connect()
    yield
    await kafka_producer.disconnect()


app = FastAPI(lifespan=lifespan)


# 添加公共中间件
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


# 路由注册（示例）
from src.apps.api.routes import health, alerts  # 确保路由模块存在

app.include_router(health.router)
app.include_router(alerts.router, prefix="/api/v1", tags=["alerts"])
