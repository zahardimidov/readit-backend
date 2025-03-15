from sqlalchemy import select

from app.infra.database.models import Book
from app.infra.database.session import async_session
from app.infra.repository.base import BaseRepository


class BookRepository(BaseRepository[Book]):
    model = Book
    session = async_session

    async def get_user_books(self, user_id):
        async with self.session() as session:
            conditions = [Book.user_id == user_id]

            books = await session.scalars(select(Book).where(*conditions))

            return books.all()
