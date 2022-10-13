from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
]



from api.v1 import routers as v1_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router.router)
app.mount("/static", StaticFiles(directory="web/dist"), name="static")
app.mount("/assets", StaticFiles(directory="web/dist/assets"), name="assets")

templates = Jinja2Templates(directory="web/dist")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})