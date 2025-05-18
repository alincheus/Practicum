import pytest
from src.storage.history import Storage
import os

storage = Storage("test_history.json")

def test_save_and_load():
    storage.save({"operation": "2 + 2", "result": 4})
    history = storage.load()
    assert history[-1]["operation"] == "2 + 2"
    assert history[-1]["result"] == 4

def test_empty_file():
    if os.path.exists("empty_history.json"):
        os.remove("empty_history.json")
    empty_storage = Storage("empty_history.json")
    assert empty_storage.load() == []

def test_multiple_saves():
    storage.save({"operation": "10 / 2", "result": 5})
    storage.save({"operation": "3 * 3", "result": 9})
    history = storage.load()
    assert len(history) >= 3  # Должно быть минимум 3 записи
