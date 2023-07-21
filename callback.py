from dto import ChatbotRequest
from samples import list_card
import aiohttp
import time
import logging

logger = logging.getLogger("Callback")

async def callback_handler(request: ChatbotRequest) -> dict:

    url = request.userRequest.callbackUrl
    payload = list_card
    time.sleep(3.0)

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=payload) as resp:
            result = await resp.json()
            logger.info("callback response from url={} json={}".format(url, result))
