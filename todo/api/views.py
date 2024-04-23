from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView


class ListAllTodo(ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class SingleTodo(UpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class CreateTodo(CreateAPIView):
    serializer_class = TodoSerializer

class DeleteTodoView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

