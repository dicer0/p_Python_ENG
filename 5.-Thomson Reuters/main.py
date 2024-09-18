# -*- coding: utf-8 -*-

import fastapi
import sse_starlette

from modules.database_models import DatabaseModels
from modules.llm import GorpAssistant
from API_Keys.Llaves_ChatGPT_Bard_etc import ChatGPT_Key, DB_Password

app = fastapi.FastAPI()

db = DatabaseModels(dbname='c1_AI_ChatHistory', user='postgres', password=DB_Password)
llm_assistant = GorpAssistant(api_key=ChatGPT_Key)

@app.on_event("shutdown")
def shutdown_event():
    db.close()

@app.get("/")
def welcome_chat():
    return "Welcome to the Gorp Assistant Chat"

@app.post("/chat/new")
def create_chat():
    chat_session_id = db.create_chat_session()
    return {"chat_session_id": chat_session_id}

@app.post("/chat/{session_id}/send")
async def send_message(session_id: int, user_message: str):
    history = db.get_chat_history(session_id)

    if history is None:
        raise fastapi.HTTPException(status_code=404, detail="Chat session not found")

    db.add_message(user_message, "user", session_id)
    stream = await llm_assistant.prompt_llm_async(user_message)

    async def stream_response():
        async for chunk in stream:
            content = chunk["choices"][0]["delta"]["content"]
            yield content

    assistant_message = ''.join([chunk async for chunk in stream_response()])
    db.add_message(assistant_message, "assistant", session_id)

    return sse_starlette.EventSourceResponse(stream_response())

@app.get("/chat/{session_id}/history")
def get_chat_history(session_id: int):
    history = db.get_chat_history(session_id)
    if not history:
        raise fastapi.HTTPException(status_code=404, detail="No messages found for this session")
    return history