from typing import Any, Dict

from models.data.mongoframes_models import Book, Category
from mongoframes.factory.makers import Q


class BookRepository:
    def insert_book(self, details: Dict[str, Any]) -> bool:
        try:
            book = Book(**details)
            book.insert()

        except Exception as e:
            print(e)
            return False
        return True

    def update_book(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            book = Book.one(Q.id == id)
            for key, value in details.items():
                setattr(book, key, value)
            book.update()
        except Exception:
            return False
        return True

    def add_category(self, id: int, category: Category) -> bool:
        try:
            book = Book.one(Q.id == id)
            book.category = category
            book.update()
        except Exception:
            return False
        return True

    def delete_book(self, id: int) -> bool:
        try:
            book = Book.one(Q.id == id)
            book.delete()
        except Exception:
            return False
        return True

    def get_all_book(self):
        books = [b.to_json_type() for b in Book.many()]
        return books

    def get_book(self, id: int):
        book = Book.one(Q.id == id).to_json_type()
        return book
