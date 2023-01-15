from pydantic import BaseModel

class CreateShop(BaseModel):
    name: str
    location: str
    productnum: int

class Shop:
    def __init__(self, id: int, name: str, location: str, productnum: int) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.productnum = productnum
        
