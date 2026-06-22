# ================================
# IMPORTS
# ================================
from listen import listen              # Handles voice input
from agent import orchestrator         # Routes tasks (AI + pipelines)
from voice import speak                # Handles text-to-speech
from memory import save_to_memory      # Stores interactions


# ================================
# OPTIONAL: SHORTEN LONG RESPONSES
# ================================
def shorten_response(text, max_length=250):
    """
    Shortens long responses for cleaner voice output
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


# ================================
# MAIN JARVIS LOOP
# ================================
def run_jarvis():

    print("🤖 Jarvis is online... (say 'exit' to stop)")
    speak("Jarvis is online. How can I help you?")

    while True:

        # ----------------------------
        # STEP 1: LISTEN FOR INPUT
        # ----------------------------
        user_input = listen()

        # Handle silence / failed recognition
        if not user_input:
            print("❌ No input detected")
            speak("I didn't catch that. Please repeat.")
            continue

        print(f"🎙️ You said: {user_input}")

        # ----------------------------
        # STEP 2: EXIT CONDITION
        # ----------------------------
        if "exit" in user_input.lower():
            speak("Shutting down. Goodbye.")
            print("👋 Jarvis stopped")
            break

        # ----------------------------
        # STEP 3: THINKING PHASE
        # ----------------------------
        print("🧠 Thinking...")

        try:
