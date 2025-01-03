from enum import Enum

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    properties: dict 

class UserRequest(BaseModel):
    utterance: str
    callbackUrl: Optional[str] = None
    user: User

class Intent(BaseModel):
    name: str

class ChatbotRequest(BaseModel):
    userRequest: UserRequest
    intent: Intent
    action: dict

class UserIdType(Enum):
    BOT_USER_KEY = "botUserKey"
    APP_USER_KEY = "appUserKey"
    PLUSFRIEND_USER_KEY = "plusfriendUserKey"

class UserForEventApi(BaseModel):
    type: UserIdType
    id: str

class EventApiParameters(BaseModel):
    botId: str
    kakaoRestApiAppKey: str
    eventName: str
    users: list[UserForEventApi]

class EventApiStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    ERROR = "ERROR"

class EventApiResponse(BaseModel):
    taskId: str
    status: EventApiStatus
    message: Optional[str] = None
    timestamp: int
