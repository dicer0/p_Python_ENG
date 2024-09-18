# -*- coding: utf-8 -*-

from modules import ChatGPT_TypeNotation
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

import asyncio
import random
import fastapi
import sse_starlette

app = fastapi.FastAPI()

@app.get("/stream-example")
async def stream_example():
    async def stream_tokens():
        for token in ['hello', ', ', 'this ', 'is ', 'a ', 'streamed ', 'response.']:
            await asyncio.sleep(random.randint(0, 3))
            print(f"Yielding token: {token}")
            yield token
    return sse_starlette.sse.EventSourceResponse(stream_tokens())