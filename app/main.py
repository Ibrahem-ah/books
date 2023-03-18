from datetime import date
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
import app.models as models


from app.database import SessionLocal, Base, engine
Base.metadata.create_all(engine)  # Creating the books table

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: date = None

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get("/books", response_model=List[Book], status_code=200)
async def getBooks():
    books = db.query(models.Book).all()
    return books


@app.get("/books/{book_id}", status_code=200)
async def getBook(book_id: int):
    book = db.query(models.Book).get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book Doesn't Exist")
    return book


@app.post("/books", response_model=Book, status_code=201)
def createBook(book: Book):
    newBook = models.Book(
        title=book.title,
        author=book.author,
        published_date=book.published_date,

    )
    db.add(newBook)
    db.commit()
    return newBook


@ app.put('/books/{book_id}', status_code=201)
def updateBook(book_id: int, book: Book):
    _book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    _book.title = book.title
    _book.author = book.author
    _book.published_date = book.published_date

    return _book


@ app.delete('/book/{book_id}', status_code=200)
async def deleteBook(book_id: int):
    _book = db.query(models.Book).get(book_id)

    if _book is None:
        raise HTTPException(status_code=404, detail="Book doesn't exist")

    db.delete(_book)
    db.commit()
    return {"This book has been delete", _book}
