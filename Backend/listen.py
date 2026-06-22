import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    print("✅ Audio captured")

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)

        print(f"✅ You said: {text}")
        return text

    except Exception as e:
        print(f"❌ Recognition error: {e}")
        return ""   # ✅ IMPORTANT: return empty instead of "ERROR"