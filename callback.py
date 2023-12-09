#-*- coding: utf-8 -*-

from dto import ChatbotRequest
from samples import simple_text_sample
import aiohttp
import time
import requests
import json
from icecream import ic

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


# def callback_handler2(request: ChatbotRequest):
#     url = request.userRequest.callbackUrl
#     ic(url)
#     payload = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "simpleText": {
#                         "text": "콜백 응답~"
#                     }
#                 }
#             ]
#         }
#     }

#     try:
#         headers = { 'Content-Type': 'application/json' }
#         res = requests.post(url, headers=headers, data=json.dumps(payload))
#         ic(res.text)
#     except Exception as e:
#         ic(e)