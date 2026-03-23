from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/website")
def website(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

