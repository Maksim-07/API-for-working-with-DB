from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    password: str
    name: str
    city: str


class UserUpdateSchema(UserSchema):
    pass
