from fastapi import FastAPI
from models import Developer , Project

app = FastAPI()

#creating developer api with post method

@app.post("/developers/")
def create_developer(developer:Developer):
    return {"message" : "developer created successfully" , "developer": developer}


#creating projects api with post method

@app.post("/projects/")
def create_project(project:Project):
    return {"message" : "Project created successfully" , "Project": project}
