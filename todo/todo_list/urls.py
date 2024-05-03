from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
]
