from fastapi import FastAPI
# from database import create_tables

from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)

def test_on_startup(capsys):
    with client:
        pass  # Startup event is triggered here
    captured = capsys.readouterr()
    assert "hi" in captured.out