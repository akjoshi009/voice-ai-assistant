# 🎙️ Voice AI Agents

An always-on voice-enabled AI Agents using:

- 🧠 **OpenAI GPT-4** for natural conversation
- 🗣️ **Deepgram** for real-time speech-to-text transcription
- 🔊 **Smallest.ai** for text-to-speech response generation

---

## 🚀 Features

- Record your voice, transcribe it, and chat with GPT-4
- Agents responds back with human-like voice
- Runs in a loop until you say **"stop"**, **"exit"**, or **"quit"**

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/voice-ai-assistant.git
cd voice-ai-assistant
```
### 🔧 Functional Enhancements
Continuous Listening (Hotword Detection)

Use a hotword like “Hey Assistant” to trigger recording instead of looping every few seconds.

Libraries: snowboy, porcupine, or Vosk.

Multilingual Support

Use Deepgram’s multilingual capabilities.

Switch OpenAI and TTS responses based on detected language.

Personalized Memory

Store user preferences, past conversations, or names using SQLite or JSON files.

Create a more context-aware assistant.

GUI Interface

Build a simple GUI using Tkinter or PyQt to start/stop conversations and display transcripts/responses.

Command Handling (Control Actions)

Recognize special commands like:

“Tell me a joke”

“What’s the weather?”

“Set a timer for 5 minutes”

Use intent classification or rule-based command parsing.

Voice Response Speed & Tone Control

Allow users to set speaking speed and pitch in Smallest.ai API parameters.

Transcription Confidence Filtering

Only respond if Deepgram confidence > 0.85 to avoid misinterpreted speech.
