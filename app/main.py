from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{items_id}")
async def read_items(item_id: int, q: Optional[str] =None):
    return {"item_id": item_id, "q": q}


if __name__ =="__main__" :
    uvicorn.run(app, port =8000, host = "0.0.0.0")