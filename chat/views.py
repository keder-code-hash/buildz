from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import User
from authentication.serializers import FetchUserSerializer
from .serializers import RoomSerializer,MessageSerializer,MessageSeenSerializer
from .models import MessageSeenMetric
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from authentication.renderers import UserRenderer
from .models import Room,Message
from django.db.models import Q
import jwt
import json
from PIL import Image
import os
from django.http import HttpResponse


def index(request):
    return render(request, "chat/index.html",{"current_host":request.get_host()})

def room(request, room_name):
    return render(request, "chat/room.html",{"current_host":request.get_host()})

def login(request):
    return render(request,"chat/auth/login.html",{"current_host":request.get_host()})

def fetchusers(request):
    users = User.objects.all()
    users_list = FetchUserSerializer(users,many=True)
    return render(request,"chat/users.html",{"users":users_list.data,"current_host":request.get_host()})


class RoomCreateView(generics.GenericAPIView):

    serializer_class = RoomSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        print("create room is called")
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True) 
        room = serializer.save()
        room_data ={
            'sender':room.sender,
            'room_id':room.room_id,
            'receiver':room.receiver
        }
        return Response(room_data, status=status.HTTP_201_CREATED)
    

class FetchMessage(generics.GenericAPIView):

    serializer_class=MessageSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        room_id = request.data.get('room_id')
        senderJwt = request.data.get('sender')
        SECRET_KEY = '@6p-h7#oy4unyb4+(@i&3eq(knbkvjkeyv&@*8+a%f45b@mfm1'
        decoded_token = jwt.decode(senderJwt, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get('user_id')
        user = User.objects.get(id=user_id)
        sender=user.email
        messages = Message.objects.filter(room_id=room_id).order_by("created_at").values() 
        msgs=json.dumps(list(messages),default=str)
        print(room_id,sender)
        room_dets = Room.objects.get(room_id=room_id,sender=sender)
        return Response({
            'sender':sender,
            'room_id':room_id,
            'messages':msgs,
            'receiver':room_dets.receiver
        }, status=status.HTTP_201_CREATED)
    
class MessageSeenView(generics.GenericAPIView):
    
    serializer_class=MessageSerializer
    renderer_classes = (UserRenderer,)

    def get(self,request,room_id,sender,receiver,message_id): 
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        valid_image=""
        try:
            message_seen = MessageSeenMetric.objects.get(room_id=room_id,sender=sender,receiver=receiver,message_id=message_id)
            messag
            valid_image = message_seen.image_link
        except MessageSeenMetric.DoesNotExist:
            valid_image = os.path.join(BASE_DIR,'static','seen_image','double_right.png')
        
        try:
            with open(valid_image, "rb") as f:
                return HttpResponse(f.read(), content_type="image/png")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/png")
            red.save(response, "PNG")
            return response