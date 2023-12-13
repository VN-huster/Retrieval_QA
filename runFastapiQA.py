from fastapi import FastAPI
import io
import uvicorn

from datetime import datetime
import response
from pydantic import BaseModel

date = datetime.now().strftime("%d-%m")
app = FastAPI()
object = "runQAĐHQG/app"


class Item(BaseModel):
    user_text: str

# FastAPI
@app.get("/")
def read_root():
    return f"Version {date}"

@app.post("/")
def return_api(text: Item):

    user_input = text.user_text
    # Get the caption
    result = response.answer(user_input)


    # Return message
    return {"message": result}

uvicorn.run(app, host="0.0.0.0", port=8706)
