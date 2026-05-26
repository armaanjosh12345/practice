const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const voiceBtn = document.getElementById('voice-btn');

const API_URL = 'http://localhost:8000/chat';

function addMessage(role, text) {
    const div = document.createElement('div');
    div.className = `message ${role}`;
    div.innerText = text;
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

async function sendMessage(text) {
    if (!text) return;

    addMessage('user', text);
    userInput.value = '';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        addMessage('jarvis', data.reply);

        if (data.execution_result) {
            console.log('Action result:', data.execution_result);
        }

        // Text to Speech
        speak(data.reply);

    } catch (error) {
        console.error('Error:', error);
        addMessage('jarvis', 'I am having trouble connecting to my backend, sir.');
    }
}

sendBtn.addEventListener('click', () => sendMessage(userInput.value));
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage(userInput.value);
});

// Voice Recognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';

    voiceBtn.addEventListener('click', () => {
        recognition.start();
        voiceBtn.style.background = 'red';
    });

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        sendMessage(transcript);
        voiceBtn.style.background = '#00e5ff';
    };

    recognition.onerror = () => {
        voiceBtn.style.background = '#00e5ff';
    };
} else {
    voiceBtn.style.display = 'none';
}

// Text to Speech
function speak(text) {
    // Remove JSON if AI included it in speech
    const cleanText = text.replace(/\{.*\}/s, '');
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
}
