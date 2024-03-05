from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import StreamingResponse


app = FastAPI()


@app.get('/')
async def root() -> {}:
    """
    Root endpoint, giving basic information about the application in return
    """
    return {"message": "Welcome to face-detection-blur-api, please use the /filters/blur endpoint following the image input to use its functionalit."}



