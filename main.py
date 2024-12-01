from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import get_db, engine
import models, schemas
from routers import auth,game

# app init
app = FastAPI()

# 정적파일 및 탬플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



# DB 모델 생성
models.Base.metadata.create_all(bind=engine)

# 라우터 설정
app.include_router(auth.router, prefix="/auth")
app.include_router(game.router, prefix="/game")

@app.get("/", response_class=HTMLResponse)
async def root():
    return templates.TemplateResponse("index.html")