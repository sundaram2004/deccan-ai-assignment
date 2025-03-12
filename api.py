"""
Entry point for API server
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.views import ner_router
from core.sentry import setup_sentry


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_sentry()

    yield


app = FastAPI(title="web-crawler", lifespan=lifespan)

# Include routers
app.include_router(ner_router)
