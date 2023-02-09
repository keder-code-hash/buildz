from django.db import models

class Room(models.Model):
    room_id = models.CharField(max_length=255,null=False,blank=False)
    sender = models.CharField(max_length=256,null=False,blank=False)
    receiver = models.CharField(max_length=256,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    room_id = models.CharField(max_length=255,null=False,blank=False)
    sender = models.CharField(max_length=256,null=False,blank=False)
    receiver = models.CharField(max_length=256,null=False,blank=False)
    message=models.CharField(max_length=255,blank=True,null=True)
    deleted_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


MESSAGE_STATUS=[
    ('SINGLE_TICK','ST'),
    ('DOUBLE_TICK','DT'),
    ('DOUBLE_BLUE_TICK','DBT'),
    ('NOT_DELIVERED','ND')
]

class MessageSeenMetric(models.Model):
    room_id = models.CharField(max_length=255,null=False,blank=False)
    sender = models.CharField(max_length=256,null=False,blank=False)
    receiver = models.CharField(max_length=256,null=False,blank=False)
    message_status = models.CharField(max_length=20,choices=MESSAGE_STATUS,default='ST')
    message_id = models.CharField(max_length=255,null=True,blank=True)
    
    image_link=models.CharField(max_length=256,null=False,blank=False)
    opening_count = models.IntegerField()
    sender_ip = models.CharField(max_length=255,null=True,blank=True)
    receiver_ip = models.CharField(max_length=255,null=True,blank=True)

    message_seen_by = models.CharField(max_length=255,blank=True,null=True)
    message_seen_at = models.DateTimeField(auto_now_add=True)
    
    deleted_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
