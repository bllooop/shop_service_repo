from fastapi import FastAPI, HTTPException
from app.shop import Shop, CreateShop


shops: list[Shop] = [
]
app = FastAPI()

def add_shops(content: CreateShop):
    id = len(shops)
    shops.append(Shop(id, content.name, content.location, content.productnum))
    return id

@app.get("/v1/shops")
async def get_shops():
    return shops


@app.post("/v1/shops")
async def add_shop(content: CreateShop):
    add_shops(content)
    return shops[-1]

@app.get("/v1/shops/{id}")
async def get_shops_by_id(id: int):
    output = [item for item in shops if item.id == id]
    if len(output) > 0:
        return output[0]
    raise HTTPException(status_code=404, detail="Shop not found")
 
@app.get("/__health")
async def check_service():
    return