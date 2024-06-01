import fastapi

from typing import Optional


app = fastapi.FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}

@app.get("/heartbeat")
async def send_heartbeat() -> fastapi.Response:
    """Health check route: sends 200 OK."""
    return fastapi.Response(status_code=200)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

