from dataclasses import dataclass
import motor.motor_asyncio

from pyrogram.types import Message
from config import DB_URL, DB_NAME
from plugins import MangaCard


class Pagination:
    pagination_id: int = 0
    
    def __init__(self):
        self.id = self.pagination_id
        Pagination.pagination_id += 1
        self.page = 1
        self.message: Message = None
        self.manga: MangaCard = None



class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.req_user = self.db.req_user

    async def add_req_user(self, context: dict):
        await self.req_user.insert_one(context)

    async def is_req_user(self, user_id: int) -> bool:
        user = await self.req_user.find_one({'user_id': user_id})
        return bool(user)


db = Database(DB_URL, DB_NAME)
