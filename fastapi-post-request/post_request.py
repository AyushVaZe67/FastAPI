import json

from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field


app = FastAPI()

class Patient(BaseModel):

    id: str
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float

def load_data():
    pass