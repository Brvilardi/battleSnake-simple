from fastapi import FastAPI, Request
import random



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/start")
async def start(data: dict):
    print(data["game"])
    return "Ready!"

@app.post("/move")
async def move(data: dict):
    choices = ["up", "down", "left", "right"]
    choice = random.choice(choices)
    return {"move": choice}

@app.post("/end")
async def end(data: dict):
    return "game ended"

