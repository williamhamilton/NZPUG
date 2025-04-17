"""
I really should document this script!
"""
# ---------------------------------------------------------------------------------------------------------------------
__author__ = "William Hamilton"
__python__ = ""
__created__ = "16/04/2025"
__copyright__ = "Copyright © 2025~"
__license__ = ""
__ToDo__ = """
- nothing to add just yet
"""

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select, create_engine, SQLModel
from models import Hero, HeroCreate

app = FastAPI()
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


@app.post("/heroes/", response_model=Hero)
def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        db_hero = Hero.from_orm(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero

@app.get("/heroes/", response_model=list[Hero])
def list_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes

@app.get("/heroes/{hero_id}", response_model=Hero)
def get_hero(hero_id: int):
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero

