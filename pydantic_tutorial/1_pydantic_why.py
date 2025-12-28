from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    linkedin_url : AnyUrl

def insert_patient_data(patient: Patient):
    print(patient.name)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print('updated')


patient_info = {'name':'Ayush','email':'a@a.a','linkedin_url':'http://linkedin.com/1322','age':'22', 'weight':'87.3', 'married':True, 'allergies':['pollen','dust','chicken'], 'contact_details':{'email':'abc@gmail.com','phone':'9988776655'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)
update_patient_data(p1)