from playwright.sync_api import sync_playwright
import os
import subprocess
import time

def run_simulation():
    # 1. Start Mock Backend
    backend_proc = subprocess.Popen(["python3", "jarvis_app/backend/mock_main.py"])
    time.sleep(2) # Wait for server to start

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 2. Open Frontend
        path = os.path.abspath("jarvis_app/frontend/index.html")
        page.goto(f"file://{path}")

        # 3. Interaction
        # Wait for greeting
        page.wait_for_selector(".jarvis")

        # Type command
        page.get_by_placeholder("Give a command...").fill("Open WhatsApp")
        page.get_by_role("button", name="SEND").click()

        # Wait for Jarvis reply
        time.sleep(2)

        # 4. Screenshot
        page.screenshot(path="/home/jules/verification/jarvis_simulation.png")
        print("Simulation screenshot saved to /home/jules/verification/jarvis_simulation.png")

        browser.close()

    # Clean up backend
    backend_proc.terminate()

if __name__ == "__main__":
    run_simulation()
