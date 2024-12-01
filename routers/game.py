from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models import Game, GameSession
from schemas import GameCreate
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/")
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = Game(
        title= game.title,
        description = game.description,
        grid_size = game.grid_size,
        words = game.words
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    
    # 링크 생성
    base_url = Request.base_url
    game_link = f"{base_url}puzzle/{db_game.id}/{db_game.title}"
    return {"game_id":db_game.id,"link":game_link,"message":"Game created successfully"}

@router.post("/{game_id}/{game_title}")
def get_game(game_id:int, game_title:str, db:Session =Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    
    