# JARVIS - Desktop AI Assistant

This is a personal AI assistant inspired by JARVIS, designed to run locally on your Precision 5550 and control your system.

## Features
- **System Control**: Mouse movement, clicking, typing, and opening applications (WhatsApp, MT5).
- **Local Brain**: Uses a local LLM to process commands and maintain memory.
- **Voice Interaction**: Speak to Jarvis and hear him respond.
- **Futuristic UI**: Electron-based desktop application.

## Prerequisites
1. **Python 3.12+**
2. **Node.js & NPM**
3. **Ollama**: To run the LLM locally without an API key.
   - Install from [ollama.com](https://ollama.com)
   - Run `ollama run llama3` to download the model.

## Setup Instructions

### 1. Backend Setup
```bash
cd jarvis_app/backend
pip install -r requirements.txt
```

### 2. Frontend/Electron Setup
```bash
cd jarvis_app/frontend
npm install
```

## Running JARVIS

### 1. Start the Backend
```bash
cd jarvis_app/backend
python main.py
```

### 2. Start the Desktop App
```bash
cd jarvis_app/frontend
npm start
```

## Usage
- **Voice**: Click the microphone icon to speak.
- **Chat**: Type commands like "Open WhatsApp" or "Move the mouse to 500, 500".
- **Trading**: You can extend `system_controller.py` to add specific MT5 strategies.

## Safety Note
This application has full access to your keyboard and mouse. Use with caution.
