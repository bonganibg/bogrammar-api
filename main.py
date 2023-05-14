import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.app import router as api_router
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), reload=os.getenv("RELOAD"))
