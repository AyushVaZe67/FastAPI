from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin:str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Palghar', 'state': 'Maharashtra', 'pin': '401440'}

add1 = Address(**address_dict)

patient_dict = {'name': 'Ayush', 'gender': 'male', 'age': 25, 'address': add1}

p1 = Patient(**patient_dict)

print(p1.name)
print(p1.address.city)