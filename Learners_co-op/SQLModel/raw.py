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
import sqlite3

app = FastAPI()

def get_conn():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def startup():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS hero (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            secret_name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.post("/heroes/")
def create_hero(hero: dict):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?)",
        (hero["name"], hero["secret_name"], hero.get("age"))
    )
    conn.commit()
    hero_id = cursor.lastrowid
    conn.close()
    return {**hero, "id": hero_id}

@app.get("/heroes/")
def list_heroes():
    conn = get_conn()
    heroes = conn.execute("SELECT * FROM hero").fetchall()
    conn.close()
    return [dict(row) for row in heroes]

@app.get("/heroes/{hero_id}")
def get_hero(hero_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hero WHERE id = ?", (hero_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Hero not found")
    return dict(row)

