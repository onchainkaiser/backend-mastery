# Query Parameters - Following the Official FastAPI Tutorial
# Learn how to handle optional parameters in URLs


# Step 1: Create an endpoint with query parameters
# TODO: Create a GET endpoint at "/items/"
# TODO: Add function parameters: skip: int = 0, limit: int = 10
# TODO: Return: {"skip": skip, "limit": limit}
# Hint: Function parameters become query parameters automatically!

# Step 2: Combine path and query parameters (from official tutorial)
# TODO: Create a GET endpoint at "/items/{item_id}"
# TODO: Add path parameter: item_id
# TODO: Add query parameter: q: str | None = None
# TODO: Return: {"item_id": item_id, "q": q}
# Hint: Mix path parameters {item_id} with query parameters q


from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def get_items(skip: int = 0, limit: int = 10):
  return {"skip": skip, "limit": limit}

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None):
  return {"item_id": item_id, "q": q}

