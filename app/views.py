from fastapi import APIRouter

from app.serializers import BaseSerializer
from nlp.predict import NERPredictor

ner_router = APIRouter()


@ner_router.post("/predict")
async def predict_ner(sentence: str) -> BaseSerializer:
    ner_predictor: NERPredictor = NERPredictor()
    tokens, predicted_tags = ner_predictor.predict(sentence)

    return BaseSerializer(
        message="NER prediction successful.",
        data={"tokens": tokens, "tags": predicted_tags},
    )
