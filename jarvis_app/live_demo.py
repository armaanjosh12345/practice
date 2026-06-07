from playwright.sync_api import sync_playwright
import os
import subprocess
import time

def run_live_demo():
    print("Initializing Quantum Sandbox Live Demo...")

    # 1. Start Mock Backend in the background
    backend_proc = subprocess.Popen(["python3", "jarvis_app/backend/mock_main.py"])
    time.sleep(3)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 2. Launch Interface
        path = os.path.abspath("jarvis_app/frontend/index.html")
        page.goto(f"file://{path}")

        print("System Greeting: 'Quantum Sandbox systems online, sir...'")
        time.sleep(2)

        # 3. Simulate Jarvis doing a market scan
        print("Jarvis: 'Running market regime analysis on XAUUSD...'")
        page.get_by_placeholder("Give a command...").fill("Run market scan")
        page.get_by_role("button", name="SEND").click()

        # 4. Capture the "Live" system state
        time.sleep(3)
        page.screenshot(path="/home/jules/verification/jarvis_live_demo.png")
        print(f"Live demo screenshot captured: /home/jules/verification/jarvis_live_demo.png")

        browser.close()

    # Clean up
    backend_proc.terminate()
    print("Demo sequence complete.")

if __name__ == "__main__":
    run_live_demo()
