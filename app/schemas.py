from pydantic import BaseModel, ConfigDict

class SearchResponse(BaseModel):
    title: str | None = None
    content: str | None = None
    content_type: str | None = None

    model_config = ConfigDict(from_attributes=True)