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
            # Send input to orchestrator (AI + pipelines)
            response = orchestrator(user_input)

        except Exception as e:
            print(f"❌ Error in processing: {e}")
            speak("Something went wrong while processing your request.")
            continue

        # ----------------------------
        # STEP 4: SAVE MEMORY
        # ----------------------------
        save_to_memory(user_input, response)

        # ----------------------------
        # STEP 5: DISPLAY RESPONSE
        # ----------------------------
        print("Jarvis:", response)

        # ----------------------------
        # STEP 6: SPEAK RESPONSE
        # ----------------------------
        try:
            spoken_response = shorten_response(response)
            print("🔊 Speaking response...")
            speak(spoken_response)
        except Exception as e:
            print(f"❌ Voice error: {e}")


# ================================
# ENTRY POINT
# ================================
if __name__ == "__main__":
    run_jarvis()