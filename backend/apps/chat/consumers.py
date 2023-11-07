from token import AWAIT

from djangochannelsrestframework import generics


class ChatConsumer(generics.AsyncAPIConsumer):
    async def connect(self):
        if not self.scope["user"]:
            await self.close()
        await self.accept()
