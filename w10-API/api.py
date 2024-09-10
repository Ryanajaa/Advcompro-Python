from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
# Define a Pydantic model for an item
class Item(BaseModel):
	name: str
	description: Union[str, None] = None
	price: float
	tax: Union[float, None] = None

# In-memory database
items = {}

@app.get("/")
def read_root():
	return {"Hello": "World"}

# GET method to read an item by item_id
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	if item_id in items:
		return {"item_id": item_id, "item": items[item_id], "q": q}
	raise HTTPException(status_code=404, detail="Item not found")

# POST method to create a new item
@app.post("/items/")
def create_item(item_id: int, item: Item):
	if item_id in items:
		raise HTTPException(status_code=400, detail="Item already exists")
	items[item_id] = item
	return {"item_id": item_id, "item": item}

# PUT method to update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
	if item_id not in items:
		raise HTTPException(status_code=404, detail="Item not found")
	items[item_id] = item
	return {"item_id": item_id, "item": item}

# DELETE method to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
	if item_id not in items:
		raise HTTPException(status_code=404, detail="Item not found")
	del items[item_id]
	return {"detail": "Item deleted"}