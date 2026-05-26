import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Mock pyautogui before importing SystemController
sys.modules['pyautogui'] = MagicMock()

from jarvis_app.backend.system_controller import SystemController
from jarvis_app.backend.brain import Brain

def test_system_controller_move_mouse():
    import pyautogui
    sc = SystemController()
    result = sc.move_mouse(100, 200)
    pyautogui.moveTo.assert_called_with(100, 200, duration=0.25)
    assert "Moved mouse to 100, 200" in result

def test_brain_memory():
    db_test = "test_memory.db"
    if os.path.exists(db_test):
        os.remove(db_test)

    brain = Brain(db_path=db_test)
    brain.store_memory("user_name", "Tony")
    assert brain.retrieve_memory("user_name") == "Tony"

    if os.path.exists(db_test):
        os.remove(db_test)

def test_brain_parse_action():
    brain = Brain()
    reply = 'Certainly! {"action": "open_whatsapp", "params": {}}'
    action = brain.parse_action(reply)
    assert action["action"] == "open_whatsapp"

def test_system_controller_execute_command():
    sc = SystemController()
    with patch.object(sc, 'open_whatsapp', return_value="Opening WhatsApp") as mock_method:
        result = sc.execute_command("open_whatsapp", {})
        mock_method.assert_called_once()
        assert result == "Opening WhatsApp"
