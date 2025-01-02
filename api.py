from fastapi import FastAPI
from dto import ChatbotRequest, EventApiParameters, EventApiResponse
import threading
import logging
import time
import requests


logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    return { "name": "Kakao Chatbot Skill Examples" }

######################################################
# Response Format Samples
######################################################

simple_text_sample = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "What is your choice?"
                }
            }
        ],
        "quickReplies": [
            {
                "messageText": "Your choice is 1.",
                "action": "message",
                "label": "choice 1"
            },
            {
                "messageText": "Your choice is 2.",
                "action": "message",
                "label": "choice 2"
            },
        ]
    }
}

simple_image_sample = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg",
                    "altText": "A treasure chest is placed on the sandy beach."
                }
            },
            {
                "simpleText": {
                    "text": "Here is your image."
                }
            }
        ]
    }
}


######################################################
# Webhook Example
######################################################

@app.post("/skill")
async def skill_example(req: ChatbotRequest):
    return simple_text_sample


######################################################
#  Callback Example
######################################################

def callback_handler(request: ChatbotRequest) -> dict:
    callback_url = request.userRequest.callbackUrl
    time.sleep(3)
    if callback_url:
        requests.post(callback_url, json=simple_image_sample)


@app.post("/callback")
async def callback_example(req: ChatbotRequest):

    threading.Thread(target=callback_handler, args=(req,)).start()

    intermediate_message = {
        "version": "2.0",
        "useCallback": True,
        "data": {
            "text" : "processing..."
        }
    }
    return intermediate_message


######################################################
#  EventAPI Using Example
######################################################

@app.post("/event-api-trigger")
async def event_api_trigger(
        req: EventApiParameters  # Parameters required for using the Event API.
):
    # The parts below are examples of what users of the Event API should implement.
    event_api_url = f'https://bot-api.kakao.com/v2/bots/{req.botId}/talk'

    headers = {
        "Authorization": f'KakaoAK {req.kakaoRestApiAppKey}',
        "Content-Type": "application/json"
    }

    data = {
        "event": {
            "name": req.eventName
        },
        "user": [
            {
                "type": user.type.value,
                "id": user.id
            } for user in req.users
        ]
    }

    response = requests.post(url=event_api_url, headers=headers, json=data)

    return EventApiResponse(**response.json())
