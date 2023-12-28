from typing import List

from pydantic import BaseModel


class TargetVoice(BaseModel):
    voice_id: int
    voice_name: str
    provider: str
    original_id: str
    sample: str
    languages: List[str]
