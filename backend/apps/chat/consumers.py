from djangochannelsrestframework import generics


class ChatConsumer(generics.AsyncAPIConsumer):
    def connect(self):
        return super().connect()
