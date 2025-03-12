from typing import Any
from pydantic import BaseModel


class BaseSerializer(BaseModel):
    message: str
    data: Any = None
