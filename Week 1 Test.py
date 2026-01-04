from fastapi import FastAPI, Path, Query

app = FastAPI(
  title="Week one test "
)

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int = Path(ge=1)):
  return {"item_id": item_id}

@app.get("/items/")
async def get_item(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=50)):
  return {"skip": skip, "limit": limit}

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int = Path(gt=0), q: str | None = Query(default=None, min_length=3, max_length=30)):
  return {"user_id": user_id, "search": q}

@app.get("/orders/{order_id}")
async def get_order_by_id(order_id: int):
  return{"order_id": order_id}

@app.get("/posts/")
async def get_post(skip: int = Query(0, ge=0, description="number of records to skip"), limit: int = Query(10, ge=1, le=20, description="Max recrods to return")):
  return {
    "message": "pagination applied",
    "skip": skip,
    "limit": limit
  }