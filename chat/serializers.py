from rest_framework import serializers
from .models import Message,Room,MessageSeenMetric
import jwt
from authentication.models import User
from django.db.models import Q

class MessageSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Message
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
    
    def create(self, validated_data):
        senderJwt=validated_data.get('sender')
        SECRET_KEY = '@6p-h7#oy4unyb4+(@i&3eq(knbkvjkeyv&@*8+a%f45b@mfm1'
        decoded_token = jwt.decode(senderJwt, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get('user_id')
        user = User.objects.get(id=user_id)
        validated_data['sender']=user.email
        if Room.objects.filter(Q((Q(sender=validated_data.get('sender')) & Q(receiver=validated_data.get('receiver')))|
               (Q(receiver=validated_data.get('sender')) & Q(sender=validated_data.get('receiver')))) ).exists() is False :
            super().create(
                    {
                        'room_id':validated_data.get('room_id'),
                        'sender':validated_data.get('receiver'),
                        'receiver':validated_data.get('sender')
                    }
                )
            return super().create(validated_data)     
        else:
            return Room.objects.get(
                sender=validated_data.get('sender'),
                receiver=validated_data.get('receiver')
            )             
        
class MessageSeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSeenMetric
        fields="__all__"

    def create(self, validated_data):
        room_id = validated_data.get('room_id')
        sender = validated_data.get('sender')
        receiver = validated_data.get('receiver')
        message_id=validated_data.get('message_id')
        message_seen = MessageSeenMetric.objects.filter(room_id=room_id,sender=sender,receiver=receiver,message_id=message_id)
        if message_seen.exists():
            message_seen_object = MessageSeenMetric.objects.get(room_id=room_id,sender=sender,receiver=receiver)
            seen_count = message_seen_object.opening_count
            message_seen_object.opening_count=seen_count+1
            message_seen_object.save()
            return message_seen_object
        return super().create(validated_data)