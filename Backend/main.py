
# ================================
# IMPORTS
# ================================

# Import memory functions (store/retrieve task history)
from memory import save_to_memory, get_memory

# Import orchestrator (decides which agent handles a task)
from agent import orchestrator

# FastAPI framework for backend API
from fastapi import FastAPI

# Middleware required to allow frontend to communicate with backend
from fastapi.middleware.cors import CORSMiddleware


# ================================
# INITIALIZE BACKEND APPLICATION
# ================================

# Create the FastAPI app (this is your server)
app = FastAPI()


# ================================
# CORS CONFIGURATION
# ================================

# Allows your browser frontend (dashboard)
# to communicate with this backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (safe for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# ================================
# MEMORY ENDPOINT (SECOND BRAIN VIEW)
# ================================

# This endpoint returns all stored tasks and responses
# Useful for debugging and future memory-based features
@app.get("/memory")
def memory():
    return {
        "memory": get_memory()
    }


# ================================
# MAIN SYSTEM ENDPOINT
# ================================

# Receives user input from frontend dashboard
@app.post("/ask")
def ask(question: str):

    # ----------------------------
    # STEP 1: SEND TO ORCHESTRATOR
    # ----------------------------
    # Orchestrator decides which agent + pipeline to use
    response = orchestrator(question)

    # ----------------------------
    # STEP 2: SAVE TO MEMORY
    # ----------------------------
    # Store task and response for future use (second brain)
    save_to_memory(question, response)

    # ----------------------------
    # STEP 3: RETURN RESPONSE
    # ----------------------------
    # Send result back to frontend UI
    return {
        "response": response
    }
