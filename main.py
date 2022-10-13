from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.v1 import routers as v1_router

app = FastAPI()

app.include_router(v1_router.router)
app.mount("/static", StaticFiles(directory="web/dist"), name="static")
app.mount("/assets", StaticFiles(directory="web/dist/assets"), name="assets")

templates = Jinja2Templates(directory="web/dist")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})