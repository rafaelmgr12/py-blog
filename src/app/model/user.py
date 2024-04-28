from pydantic import BaseModel, EmailStr


class UserRequestCreate(BaseModel):
    
    name: str
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True
        
        
class UserResponse(BaseModel):
        
        id: str
        name: str
        email: EmailStr
        __created_at: str
        __updated_at: str
        
        
        class Config:
            orm_mode = True