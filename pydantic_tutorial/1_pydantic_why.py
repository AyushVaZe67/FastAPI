from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def 

patient_info = {'name':'ayush','age':22}

p1 = Patient