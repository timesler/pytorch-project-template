from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def desc():
    return {"message": "Hello world!"}