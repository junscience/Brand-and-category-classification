from pydantic import BaseModel
from typing import List


class RequestParams(BaseModel):
    params: List[str]


class ResponsePredict(BaseModel):
    params: List[str]
    predict: List[str]
    predict_quality: List[str]