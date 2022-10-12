from fastapi import FastAPI

from api.v1 import routers as v1_router

app = FastAPI()

app.include_router(v1_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}