from fastapi import FastAPI, Request
import random

app = FastAPI()

# Configuration
SNAKE_NAME = "noob"
BOARD_SIZE = {'x': 11, 'y': 11}

MOVEMENTS = []
POSSIBLE_MOVEMENTS = []

########################

# Functions and objects
POSITIONS = {
    'up': {'x': 0, 'y': 1},
    'down': {'x': 0, 'y': -1},
    'left': {'x': -1, 'y': 0},
    'right': {'x': 1, 'y': 0}
}


def movesThatWontColideItself(moves=["up", "down", "left", "right"], body=None, head=None):
    """
    Returno possible moves that the snake can perform without hitting itself
    :param moves: possible moves, default: ["up", "down", "left", "right"]
    :param body: list of the body pieces provided on API
    :param head: head of snake provided on API
    :return: possible moves that won't hit the snake
    """
    tempMoves = moves
    print(f"head: {head}")
    print(f"body: {body}")
    for bodyPiece in body:
        for move in moves:
            if (head['x'] + POSITIONS[move]['x'] == bodyPiece['x']) and (
                    head['y'] + POSITIONS[move]['y'] == bodyPiece['y']):
                tempMoves.remove(move)
    print(f"Wont colide itself: {tempMoves}")
    return tempMoves


def movesThatWontColideBoard(moves=["up", "down", "left", "right"], head=None):
    tempMoves = moves
    if head['x'] == 0:
        if "left" in tempMoves: tempMoves.remove("left")
    if head['x'] == BOARD_SIZE['x'] - 1:
        if "right" in tempMoves: tempMoves.remove("right")
    if head['y'] == 0:
        if "down" in tempMoves: tempMoves.remove("down")
    if head['y'] == BOARD_SIZE['y'] - 1:
        if "up" in tempMoves: tempMoves.remove("up")

    print(f"Wont colide board: {tempMoves}")
    return tempMoves


########################


@app.get("/")
async def root():
    obj = {'apiversion': "1",
           'author': "bvilardi",
           'color': "#9999",
           'head': "default",
           'tail': "default"}
    return obj


@app.post("/start")
async def start(data: dict):
    print("Game start!")
    # print(data["game"])
    return "Ready!"


@app.post("/move")
async def move(data: dict):
    print("Move!")
    # print(data)
    choices = ["up", "down", "left", "right"]
    me = data['you']
    betterChoices = movesThatWontColideItself(moves=choices, body=me['body'][:-1], head=me["head"]) #['body'][:-1] removes tail
    betterChoices = movesThatWontColideBoard(moves=betterChoices, head=me["head"])
    print(f"Better choices: {betterChoices}")

    choice = random.choice(betterChoices)
    MOVEMENTS.append(choice)
    POSSIBLE_MOVEMENTS.append(betterChoices)
    print(f"My choice: {choice}")
    return {"move": choice}


@app.post("/end")
async def end(data: dict):
    print("End!")
    # print(f"movements: {MOVEMENTS}\nPossible: {POSSIBLE_MOVEMENTS}")
    # print(data)
    return "game ended"
