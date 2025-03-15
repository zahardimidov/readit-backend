from app.infra.repository import BookRepository


class BookService:
    repo = BookRepository()

    async def get_user_books(self, user_id):
        return await self.repo.get_user_books(user_id=user_id)
