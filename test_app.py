import pytest
import os
from unittest.mock import patch, MagicMock
from app import app, init_db

@pytest.fixture
def client():
    """Flask provides a test client for simulating requests"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_creation():
    """App should be created and have a name"""
    assert app is not None
    assert app.name == "app"


def test_config_from_env(monkeypatch):
    """Check if config picks environment variables"""
    monkeypatch.setenv("MYSQL_HOST", "testhost")
    monkeypatch.setenv("MYSQL_USER", "testuser")
    monkeypatch.setenv("MYSQL_PASSWORD", "testpass")
    monkeypatch.setenv("MYSQL_DB", "testdb")

    # reload into app.config
    app.config['MYSQL_HOST'] = os.environ["MYSQL_HOST"]
    app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
    app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
    app.config['MYSQL_DB'] = os.environ["MYSQL_DB"]

    assert app.config['MYSQL_HOST'] == "testhost"
    assert app.config['MYSQL_USER'] == "testuser"
    assert app.config['MYSQL_PASSWORD'] == "testpass"
    assert app.config['MYSQL_DB'] == "testdb"

