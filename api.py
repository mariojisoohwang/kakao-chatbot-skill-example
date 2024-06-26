#-*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi import BackgroundTasks
from fastapi.responses import HTMLResponse
from dto import ChatbotRequest
from samples import simple_text_sample, basic_card_sample, commerce_card_sample
from callback import callback_handler
import threading

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-16s %(levelname)-8s %(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def home():
    page = """
    <html>
        <body>
            <h2>카카오 챗봇빌더 스킬 예제입니다 : )</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=page, status_code=200)

@app.post("/skill/hello")
async def sample1(req: ChatbotRequest):
    return simple_text_sample

@app.post("/skill/basic-card")
async def sample2(req: ChatbotRequest):
    return basic_card_sample

@app.post("/skill/commerce-card")
async def sample3(req: ChatbotRequest):
    return commerce_card_sample

@app.post("/callback")
async def callback1(req: ChatbotRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(callback_handler, req)
    out = { "version": "2.0", "useCallback": True }
    return out


# @app.post("/callback2")
# async def callback2(req: ChatbotRequest, background_tasks: BackgroundTasks):
#     thread = threading.Thread(target=callback_handler2, args=(req,))
#     thread.start()

#     out = {
#         "version" : "2.0",
#         "useCallback" : True,
#         "data": {
#             "text" : "생각하고 있는 중이에요😘 \n15초 정도 소요될 거 같아요 기다려 주실래요?!"
#         }
#     }
#     return out
