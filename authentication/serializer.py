from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        feilds = ['id', 'username', 'password', 'email', 'firstname', 'lastname']
    
