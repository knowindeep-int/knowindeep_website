import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from project.models import Profile
from asgiref.sync import sync_to_async



class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        user = self.scope["user"]
        await self.updateStatus(user, True)

        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("received", event)
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    async def websocket_disconnect(self, event):
        user = self.scope["user"]
        await self.updateStatus(user, False)

    @database_sync_to_async
    def updateStatus(self, user, online: bool):
        print(user)
        print("here")
        profile = Profile.objects.get(user = user)
        profile.isOnline = online
        profile.save()