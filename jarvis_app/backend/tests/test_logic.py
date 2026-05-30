import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Mock pyautogui before importing SystemController
sys.modules['pyautogui'] = MagicMock()

from system_controller import SystemController
from brain import Brain

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

def test_system_controller_open_url():
    import webbrowser
    from unittest.mock import patch
    sc = SystemController()
    with patch('webbrowser.open') as mock_open:
        result = sc.open_url("https://www.google.com")
        mock_open.assert_called_with("https://www.google.com")
        assert "Opening URL: https://www.google.com" in result

def test_system_controller_execute_open_url():
    sc = SystemController()
    from unittest.mock import patch
    with patch.object(sc, 'open_url', return_value="Opening URL") as mock_method:
        result = sc.execute_command("open_url", {"url": "https://www.google.com"})
        mock_method.assert_called_once_with("https://www.google.com")
        assert result == "Opening URL"
