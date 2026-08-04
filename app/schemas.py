from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str
    country: str | None = None

class AuthorOut(AuthorCreate):
    id: int
    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    price: float
    stock: int = 0
    author_id: int
    genre: str | None = None

class BookUpdate(BaseModel):
    title: str | None = None
    price: float | None = None
    stock: int | None = None
    genre: str | None = None

class BookOut(BaseModel):
    id: int
    title: str
    price: float
    stock: int
    author_id: int
    genre: str | None = None
    class Config:
        from_attributes = True