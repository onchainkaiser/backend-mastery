from fastapi import Path, FastAPI, Query

app = FastAPI(
  title= "learning Path Parameters and Numeric Validations"
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/{item_id}")
async def get_items(item_id: int = Path(ge=1)):
  return {"item_id": item_id}

@app.get("/items/{item_id}/details")
async def get_items_details(item_id: int = Path(ge=1, le=1000, description="The ID of the item"), q: str | None = Query(default=None, max_length=50)):
  return {"item_id": item_id, "q": q, "details": "item details here"}

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(title="User ID", description="The id of the user to get", ge=1)):
  return {"user_id": user_id, "message": f"User {user_id} profile"}