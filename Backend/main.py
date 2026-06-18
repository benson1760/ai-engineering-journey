from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later we lock this down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.post("/ask")
def ask(question: str):
    if "ai" in question.lower():
        return {"response": "Start with Python, APIs, and building projects"}
    return {"response": f"You asked: {question}"}