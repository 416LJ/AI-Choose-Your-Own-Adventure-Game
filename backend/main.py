from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.config import settings

from routers import story,job
from db.database import create_tables

create_tables()

#create the FASTAPI app
app = FastAPI(
    title="AI Stories", # give it a title
    description="ChatGPT choose your own adventure", # give a description
    version="0.1.0",
    docs_url="/docs", # can be anything
    redoc_url="/redoc", # can be anything
)

# add the cors middleware to the FASTAPI app
# the comment below removes a warning that pycharm ide gives for cors middleware
# noinspection PyTypeChecker
# CORS is a Cross origin resource sharing library that allows external ip addresses to access this api backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS, # loaded from the settings object created from the config file in core.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router,prefix=settings.API_PREFIX)
app.include_router(job.router,prefix=settings.API_PREFIX)

if __name__ == "__main__":
    # start the FASTAPI using the uvicorn webserver
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)



