from django.urls import path
from .views import ListAllTodo, SingleTodo, CreateAPIView, DeleteTodoView

urlpatterns = [
    path('api/todo/getAll', ListAllTodo.as_view(), name="list-all-todo" ),
    path('api/todo/get/<str:pk>', SingleTodo.as_view(), name= 'list-single-todo'),
    path('api/todo/create', CreateAPIView.as_view(), name='create-todo'),
    path('todos/<str:pk>/delete/', DeleteTodoView.as_view(), name='delete_todo'),

]
