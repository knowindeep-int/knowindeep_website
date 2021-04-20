import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from project.models import Profile
from asgiref.sync import sync_to_async
from datetime import datetime


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        user = self.scope["user"]
        # await self.updateStatus(user, True)
        await self.increaseUsers(user)
        
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
        # await self.updateStatus(user, False)
        await self.decreaseUsers(user)
        # now = datetime.now().time()
        # print(now)

    @database_sync_to_async
    def updateStatus(self, user, online: bool):
        print(user)
        print("here")
        profile = Profile.objects.get(user = user)
        profile.isOnline = online
        profile.save()

    @database_sync_to_async
    def increaseUsers(self,user):
        print(user)
        profile = Profile.objects.get(user = user)
        profile.no_of_users +=1
        print(profile.no_of_users)
        profile.save()
        now = datetime.now().time()
        print(now)
    
    @database_sync_to_async
    def decreaseUsers(self,user):
        print(user)
        profile = Profile.objects.get(user = user)
        profile.no_of_users -=1
        print(profile.no_of_users)
        now = datetime.now().time()
        print(now)
        profile.save()