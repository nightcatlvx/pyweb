import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from src.apps.api.main import app


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def mock_kafka_producer():
    mock = AsyncMock()
    mock.produce = AsyncMock()
    return mock
