#-*- coding: utf-8 -*-

from dto import ChatbotRequest
import aiohttp

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


async def callback_handler(request: ChatbotRequest) -> dict:
    url = request.userRequest.callbackUrl
    logger.info(f"callback url: {url}")
    payload = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요! 저는 챗봇입니다."
                    }
                }
            ]
        }
    }
    if url:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=payload) as resp:
                r = await resp.json()
                logger.info(f"response: {r}")