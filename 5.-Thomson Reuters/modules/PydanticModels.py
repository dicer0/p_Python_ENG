# -*- coding: utf-8 -*-

import pydantic 

class ChatMessage(pydantic.BaseModel):
    role: str
    content: str

class ChatSession(pydantic.BaseModel):
    session_id: str
    messages: list[ChatMessage]