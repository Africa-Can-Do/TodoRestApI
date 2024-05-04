from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet): # new
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
