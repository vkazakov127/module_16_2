# -*- coding: utf-8 -*-
# module_16_2.py
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def wellcome():
    return {"message": "Hello Urban!"}


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter user name",
                        example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description="Enter age",
                        example=62)]):
    return {"message": f"Username={username}; age={age}"}


@app.get("/user/{user_id}")
async def get_user_number(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=6)]):
    return {"message": f"user_id={user_id}"}
