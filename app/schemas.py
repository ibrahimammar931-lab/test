from pydantic import BaseModel, Field


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


class BookUpdate(BaseModel):
    title: str | None = None
    price: float | None = None
    stock: int | None = None


class BookOut(BaseModel):
    id: int
    title: str
    price: float
    stock: int
    author_id: int

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: str


class ReviewOut(BaseModel):
    id: int
    book_id: int
    rating: int
    comment: str

    class Config:
        from_attributes = True
