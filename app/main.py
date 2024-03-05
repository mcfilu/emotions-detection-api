from fastapi import FastAPI
from routers import filters


app = FastAPI()
app.include_router(filters.router)

@app.get('/')
async def root() -> {}:
    """
    Root endpoint, giving basic information about the application in return
    """
    return {"message": "Welcome to face-detection-blur-api, please use the /filters/blur endpoint following the image input to use its functionalit."}



