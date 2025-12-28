from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print('updated')


patient_info = {'name':'Ayush','age':'22', 'weight':'87.3', 'married':True, 'allergies':['pollen','dust','chicken'], 'contact_details':{'email':'abc@gmail.com','phone':'9988776655'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)
update_patient_data(p1)