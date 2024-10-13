from fastapi import FastAPI, HTTPException
from alumnes_db import get_all_alumnes
from alumnes import format_all_alumnes

app = FastAPI()

@app.get("/alumne/list")
def list_alumnes():
    try:
        alumnes = get_all_alumnes()
        formatted_alumnes = format_all_alumnes(alumnes)
        return formatted_alumnes
    except Exception as e:
        print(f"Error al obtenir la llista d'alumnes: {e}")
