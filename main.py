from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "rahul"}

@app.get('/first')
def first():
    return {'this is fast api : mix of first server' : 'wellcome'}


@app.get('/second')
def second():
    return {'message':'this is second page'}

@app.get('/second/{name}')
def first_name(name:str):
    return {'message':'grover'}



@app.get("/users")
def get_users():
    return ["user1", "user2"]



@app.get("/users/{user_id}")
def krishna(user_id: int):
    return {"user_id": user_id}

@app.get('/third')
def krishna():
    return {'this is third page':'welcome'}

@app.get('/third/{name}')
def krisna(name : str, age : int):
    return {f'welcome to india this is {name}': f'and i am {age} old'}




@app.get("/users")
def get_users():
    return ["user1", "user2"]



'this is main.py pulling in new document'