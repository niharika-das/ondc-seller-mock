import os
from fastapi import FastAPI

from routers.mobility_seller import router

app = FastAPI()

app.include_router(router=router)


@app.get("/")
async def root():
    return {"message": "Mobility Mock Seller!!"}


if __name__ == "__main__":
    app.run(app, port=8000)
