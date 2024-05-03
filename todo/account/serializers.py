from rest_framework import serializers
from .models import CustomUser
from todo_list.models import Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'department', 'phone_number']
        read_only_fields = ['username']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

