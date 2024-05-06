from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from account.permissions import IsOwnerOrAdminOrReadOnly

class TodoListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
