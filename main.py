from __future__ import annotations

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from fastapi import FastAPI

app = FastAPI()

data = {
    "email": "abc@mail.com",
    "bio": "Я пирожок вкусный",
    "age": 12,

}

data_wo_age = {
    "email": "abc@mail.com",
    "bio": "Я пирожок вкусный",
    # "gender": "male",
    # "birdthday": "2022"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)

    model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Юзер добавлен"}


@app.get("/users")
def get_user() -> list[UserSchema]:
    return users


# class UserAgeSchema(UserSchema):
#     age: int = Field(ge=0, le=130)

# print(repr(UserSchema(**data_wo_age)))
# print(repr(UserAgeSchema(**data)))
