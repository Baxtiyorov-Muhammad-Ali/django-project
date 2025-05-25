# dashboard/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'product_group'

        # Ulanishni qabul qilish
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Ulanishni uzish
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Olingan ma'lumotni qayta ishlash
        data = json.loads(text_data)
        message = data['message']

        # Boshqa barcha aloqalar bilan xabarni yuborish
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Boshqalariga xabar yuborish
        message = event['message']

        # WebSocket orqali xabarni yuborish
        await self.send(text_data=json.dumps({
            'message': message
        }))
