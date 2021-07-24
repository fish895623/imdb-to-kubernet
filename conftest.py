import pytest
from app import flask_app

@pytest.fixture
def app():
    return flask_app()
