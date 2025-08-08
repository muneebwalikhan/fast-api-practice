from fastapi import FastAPI
import uvicorn
from typing import Optional, Annotated
from pydantic import BaseModel,StrictInt
from enum import Enum


app = FastAPI()

# we can types for each intity inside the object dic
# class Todos(BaseModel):
#     id:int
#     name:str = "default value..."
#     desc:str
    
# using the Todos class Types help of pydyntic
# car:Todos = {
#     "id": 1,
#     "name": "Toyota",
#     "desc": "This is a car"
# }

# using Annotated we can define type and also info about the varaible like below
# studentName:Annotated[str, "This is a student name"] = "John Doe"


# students = [
#     {"id": 1, "name": "John Doe", "age": 20},
#     {"id": 2, "name": "Rode Bash", "age": 21},
#     {"id": 3, "name": "Jane Doe", "age": 22},
#     {"id": 4, "name": "John Doe", "age": 23},
#     {"id": 5, "name": "Rode Bash", "age": 24},
#     {"id": 6, "name": "Jane Doe", "age": 25},
# ]


# @app.get("/students")
# def get_students():
#     return students

# @app.post("/add-student")
# def add_student(name:str,age:int):
#     students.append({"id": len(students) + 1, "name": name, "age": age})
#     return students

# @app.put("/update-student")
# def update_student(st_id:int,name:str, age:int):
#     for std in students:
#         if std["id"] == st_id:
#             std["name"] = name
#             std["age"] = age
#     return students

# @app.delete("/remove-student")
# def remove_student(st_id):
#     for std in students:
#         if std["id"] == int(st_id):
#             students.remove(std)
#     return students

# @app.get("/filter-students")
# def filter_students(age: int,name:Optional[str]=None):
#     results = []
#     for std in students:
#         age_matched = std["age"] == age
#         name_matches = std["name"] == name if name is not None else True
#         if age_matched and name_matches:
#             results.append(std)
#     if len(results) == 0:
#         return {"message": "No students found"}
#     return results



# @app.get("/")
# def home():
#     print("Welcome to the Fast API")
#     return {"message": "Welcome to the Fast API"}

# @app.get("/todos")
# def get_todos():
#     obj = {"id": 1, "task": "Learn FastAPI"}
#     print("Getting all todos")
#     print("Getting")
#     return  {"data": obj}

# @app.put("/update-todos")
# def update_todos():
#     print("updating the todos...")
#     return {"message": "updating the todos..."}

# @app.delete("/dynamic-path/{id}")
# def dynamicPath(id):
#     print("dynamic path id...",id)
#     return id

# @app.post("/query-params")
# def query_params(username:str, age:int):
#     print("my username is: ",username + " and my age is: " + str(age))
#     return {"username": username, "age": age}




# we can define enums for paths and then we can only pass from those enums only not other data
class AssignmentId(int,Enum):
    one = 1
    two = 2
    three = 3

# body parameters it means to send json data from frontend
class DataStudent(BaseModel):
    username:str
    count:StrictInt
    data:Optional[str] = None

# path , query , body demo all included in below
# Question: how Api understand the it is path , query or body
# Answer: Api understand [path] when it pass to the route url [/student/{id}/assigments/{assigment_id}] | query by its single 
# type ex: [this_is_query:int] 
# the type is single so it is consider as query | body when we use a Base Model of pydantic so api understand it is body ex: [data:DataStudent]

@app.post("/student/{id}/assigments/{assigment_id}")  # path parameters
def student_assigments(id,assigment_id:AssignmentId, thisisbody:DataStudent, this_is_query:int):
    print("body: ",thisisbody)
    print("query data", this_is_query)
    if assigment_id is AssignmentId.three:
        return {"message": f"std id: {id} This is the third assigment"}
    if assigment_id is AssignmentId.two:
        return {"message": f"std id: {id} This is the second assigment"}
    if assigment_id is AssignmentId.one:
        return {"message": f"std id: {id} This is the first assigment"}

def start():
    print("Starting the Uvicorn server...")
    uvicorn.run("src.todos.main:app", host="127.0.0.1", port=8080,reload=True)