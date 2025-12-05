from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
from rag import RAG

app = FastAPI(title="Cloud RAG Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = RAG()

class ChatRequest(BaseModel):
    message: str

@app.post('/chat')
async def chat(req: ChatRequest):
    resp = await rag.answer(req.message)
    return {"answer": resp}

@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    task = asyncio.create_task(
        rag.index_bytes(contents, filename=file.filename)
    )
    return {
        "status": "indexing_started",
        "filename": file.filename
    }

@app.get('/health')
async def health():
    return {"status": "ok"}
