import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .serializers import MessageSerializer,MessageSeenSerializer
import os
from .util import get_client_ip_address

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        print(self.scope["user"])
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        serializer = MessageSerializer(data=text_data_json)
        serializer.is_valid(raise_exception=True)
        saved_message = serializer.save()
        # creating message seen metrics record for tracking message seen record
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        valid_image = os.path.join(BASE_DIR,'static','seen_image','double_right.png')
        messsage_seen_metric={
            'room_id' :text_data_json.get('room_id',None),
            'sender' :text_data_json.get('sender',None),
            'receiver' :text_data_json.get('receiver',None),
            'message_status' :'DOUBLE_TICK',
            'message_id' :saved_message.id,
            'image_link':valid_image,
            'opening_count':1,
            'sender_ip' :'',
            'receiver_ip' :'',
            'message_seen_count':0
        }
        message_seen_serializer = MessageSeenSerializer(data=messsage_seen_metric)
        message_seen_serializer.is_valid(raise_exception=True)
        message_seen_serializer.save()

        # print(self)
        # # print(text_data_json)
        message = text_data_json["message"] 
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message,'receiver': text_data_json.get('receiver'), 'sender': text_data_json.get('sender'),"message_id":saved_message.id}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        print(event)
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message,'receiver': event.get('receiver'), 'sender': event.get('sender'),"message_id":event.get('message_id')}))