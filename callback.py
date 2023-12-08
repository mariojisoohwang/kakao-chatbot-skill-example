#-*- coding: utf-8 -*-

from dto import ChatbotRequest
from samples import simple_text_sample
import aiohttp
import time

async def callback_handler(request: ChatbotRequest) -> dict:

    time.sleep(1.0)

    url = request.userRequest.callbackUrl

    payload = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "콜백 응답~"
                    }
                }
            ]
        }
    }

    if url:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=payload) as resp:
                await resp.json()