import os
import wave
import sounddevice as sd
import numpy as np
import openai
from dotenv import load_dotenv
from deepgram import Deepgram
from smallest import Smallest
from io import BytesIO
from scipy.io.wavfile import read as read_wav


# Load environment variables
load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SMALLEST_API_KEY = os.getenv("SMALLEST_API_KEY")

# Initialize API clients
openai.api_key = OPENAI_API_KEY
dg_client = Deepgram(DEEPGRAM_API_KEY)
smallestd = Smallest(api_key=SMALLEST_API_KEY)

# Function to record audio from the microphone
def record_audio(duration=5, filename="input.wav"):
    fs = 44100  # Sampling rate
    print("🎙️ Recording... Speak now.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())
    print("✅ Recording saved.")
    return filename

# Function to transcribe audio using Deepgram
def transcribe(filename):
    with open(filename, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = dg_client.transcription.sync_prerecorded(source, {'punctuate': True})
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        print(f"🧑 You said: {transcript}")
        return transcript

# Function to get a response from OpenAI
def chat_with_openai(prompt):
    system_msg = "You are a helpful and friendly travel advisor."
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response['choices'][0]['message']['content']
    print(f"🤖 Travel Advisor: {reply}")
    return reply

# Function to convert text to speech using Smallest's WavesClient
def speak_with_smallest(text):
    try:
            print(f"Agent: {text}")
            
            tts_response = smallestd.synthesize(
                text=text,
                model="lightning",
                speed=1.0,
                sample_rate=24000,
                add_wav_header=True
            )
            
            with BytesIO(tts_response) as audio_buffer:
                fs, data = read_wav(audio_buffer)
                #chunk_size = 4096
                #chunk = data[i:i+chunk_size]
                sd.play(data, fs)
                sd.wait()
    except Exception as e:
            print(f"TTS error: {e}")
    

if __name__ == "__main__":
    while True:
        audio_file = record_audio()
        user_input = transcribe(audio_file)
        
        if user_input.strip().lower() in ["stop", "exit", "quit"]:
            print("🛑 Exiting conversation. Goodbye!")
            break
        
        if user_input.strip():
            ai_response = chat_with_openai(user_input)
            speak_with_smallest(ai_response)
