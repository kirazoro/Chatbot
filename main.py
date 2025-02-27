from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from api_handler import get_nemotron_response

app = FastAPI()

# Serve HTML templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Message(BaseModel):
    message: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_response")
async def get_response(user_input: Message):
    bot_response = await get_nemotron_response(user_input.message)
    return {"response": bot_response}
