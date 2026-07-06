import pyautogui
import subprocess
import platform
import os
import webbrowser

class SystemController:
    def __init__(self):
        # Disable fail-safe if needed, but it's safer to keep it on
        # pyautogui.FAILSAFE = True
        pass

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y, duration=0.25)
        return f"Moved mouse to {x}, {y}"

    def click(self, x=None, y=None):
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()
        return "Clicked"

    def type_text(self, text):
        pyautogui.write(text, interval=0.1)
        return f"Typed: {text}"

    def press_key(self, key):
        pyautogui.press(key)
        return f"Pressed {key}"

    def open_application(self, app_path_or_command):
        try:
            if platform.system() == "Windows":
                os.startfile(app_path_or_command)
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", app_path_or_command])
            else:  # Linux
                subprocess.Popen([app_path_or_command])
            return f"Opening {app_path_or_command}"
        except Exception as e:
            return f"Error opening {app_path_or_command}: {str(e)}"

    def open_whatsapp(self):
        # This is a simplification; actual path depends on installation
        return self.open_application("whatsapp")

    def open_mt5(self):
        # This is a simplification; actual path depends on installation
        return self.open_application("metatrader5")

    def browse(self, url):
        try:
            # Use webbrowser module for cross-platform safety and to avoid shell injection.
            webbrowser.open(url)
            return f"Opened browser to {url}"
        except Exception as e:
            return f"Error opening browser: {str(e)}"

    def get_screen_size(self):
        width, height = pyautogui.size()
        return {"width": width, "height": height}

    def execute_command(self, action, params):
        if action == "move_mouse":
            return self.move_mouse(params.get("x"), params.get("y"))
        elif action == "click":
            return self.click(params.get("x"), params.get("y"))
        elif action == "type":
            return self.type_text(params.get("text"))
        elif action == "press":
            return self.press_key(params.get("key"))
        elif action == "open_whatsapp":
            return self.open_whatsapp()
        elif action == "open_mt5":
            return self.open_mt5()
        elif action == "browse":
            return self.browse(params.get("url"))
        else:
            return "Unknown action"
