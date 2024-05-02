import alembic
from pydantic import BaseModel, Field


class BlogPostRequestCreate(BaseModel):
    
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    user_id: str = Field(..., min_length=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "My awesome blog post",
                "content": "This is the content of my awesome blog post",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }
        
class BlogPostResponse(BaseModel):
    id: str
    title: str
    content: str
    user_id: str
    created_at: str
    updated_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "title": "My awesome blog post",
                "content": "This is the content of my awesome blog post",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "__created_at": "2021-01-01T12:00:00",
                "__updated_at": "2021-01-01T12:00:00",
            }
        }
    