from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a model for the input
class InputData(BaseModel):
    name: str

@app.post("/greet/")
async def greet_user(input_data: InputData):
    return {"message": f"Hello, happy exams time February {input_data.name}!"}
