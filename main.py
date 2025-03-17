from fastapi import FastAPI
import random

app = FastAPI()

pakistani_jokes = [
    {"setup": "Why did the Pakistani developer refuse to use Python?", "punchline": "Because he couldn't handle the 'indentation' drama!"},
    {"setup": "How does a Lahori programmer fix a bug?", "punchline": "He adds more spices and refactors the code!"},
    {"setup": "What did the Karachi server say when it crashed?", "punchline": "'Load shedding ho gayi bhai!'"},
    {"setup": "Why don’t Pakistani students like Java?", "punchline": "Because they prefer 'chai' over Java!"},
    {"setup": "What’s a Punjabi coder’s favorite loop?", "punchline": "‘Do while thand hai’"}
]


@app.get("/pakistani_jokes")
def get_random_joke():
    """Returns a random Pakistani joke"""
    return {"pakistani_jokes":random.choice(pakistani_jokes)}
