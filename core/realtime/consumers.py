# core/realtime/consumers.py

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class UserConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]

        if not user or user.is_anonymous:
            await self.close()
            return

        self.group_name = f"user_{user.id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

        await self.send_json({
            "type": "connected",
            "user_id": str(user.id),
            "full_name": user.full_name,
            "email": user.email,
        })

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def receive(self, text_data=None, bytes_data=None):
        await self.send_json({
            "type": "pong",
            "message": "received",
        })

    # ==================================================
    # GENERIC NOTIFICATION EVENT
    # group_send(type="notify")
    # ==================================================
    async def notify(self, event):
        await self.send_json({
            "type": "notification",
            "data": event["data"],
        })

    # ==================================================
    # NEW STANDARD EVENT
    # group_send(type="ws.notification")
    # ==================================================
    async def ws_notification(self, event):
        await self.send_json({
            "type": "notification",
            "data": event["payload"],
        })

    # ==================================================
    # OPTIONAL GENERIC MESSAGE
    # group_send(type="ws.message")
    # ==================================================
    async def ws_message(self, event):
        await self.send_json(event["payload"])

    
    async def chat_message(self, event):
        await self.send_json({
            "type": "chat.message",
            "room_id": event["room_id"],
            "id": event["id"],
            "sender_id": event["sender_id"],
            "content": event["content"],
            "created_at": event["created_at"],
            "status": event["status"],
        })


    async def chat_typing(self, event):
        await self.send_json(event["data"])