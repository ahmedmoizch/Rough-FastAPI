import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/account")
async def account(request: Request):
    
    return templates.TemplateResponse("account.html", {"request": request})

@app.get("/login")
def login(request: Request):

    return templates.TemplateResponse("login.html", {"request": request})

# Local Server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)