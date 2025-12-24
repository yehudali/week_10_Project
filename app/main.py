from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from data_interactor1 import DataInteractor


db = DataInteractor()

app = FastAPI()

class ContactCreate(BaseModel):
    first_name : str
    last_name : str
    phone_number : str

class ContactUpdate(BaseModel):
    id : str
    first_name : 

    last_name : str
    phone_number : str

class ContactOut(BaseModel):
    id : str

@app.get("/")
def hello():
    return{"maseg" : "hiii!" }

@app.get("/contacts")
def get_all_contacts1():
    return db.get_all_contacts()


@app.post("/contacts")
def create_new_contact(parameters:ContactCreate):
    return db.creat_contact(first_name=parameters.first_name, last_name=parameters.last_name, phone_number=parameters.phone_number)

@app.put("/contacts/{id}")
def update_existing_contact(id,parameters:ContactCreate):
    return db.update_contact(id,first_name=parameters.first_name, last_name=parameters.last_name, phone_number=parameters.phone_number)

@app.delete("/contacts/{id}")
def delete_contact(id):
    return db.delet_contact(id)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8001)