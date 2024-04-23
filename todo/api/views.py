from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView


class ListAllTodo(ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class SingleTodo(RetrieveDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class CreateTodo(CreateAPIView):
    serializer_class = TodoSerializer
