from fastapi import FastAPI, Request
import random

app = FastAPI()


@app.get("/")
async def root():
    obj = {'APIVersion': "1",
           'Author': "bvilardi",
           'Color': "#888888",
           'Head': "default",
           'Tail': "default"}
    return obj


@app.post("/start")
async def start(data: dict):
    print("Game start!\n", data["game"])
    return "Ready!"


@app.post("/move")
async def move(data: dict):
    print("Move!\n", data)
    choices = ["up", "down", "left", "right"]
    choice = random.choice(choices)
    return {"move": choice}


@app.post("/end")
async def end(data: dict):
    print("End!\n", data)
    return "game ended"
