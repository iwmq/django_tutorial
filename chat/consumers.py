import json

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.send(
            "test-print",
            {
                'type': 'test.print',
                'text': 'hello'
            }
        )

        print(f"Connected")
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print(f"Connection closed because: {close_code}")

    async def receive(self, text_data):
        """
        Receive message from websocket
        """
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': message
            }
        )

        print(f"Received message: {message}")

    async def chat_message(self, event):
        """
        Receive message from room group
        """
        message = event['message']
        print(f"Received group message: {message}")

        # Send message to websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


class PrintConsumer(AsyncConsumer):
    async def test_print(self, message):
        print(f"Test: {message['text']}")