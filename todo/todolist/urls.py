from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoListViewSet

router = SimpleRouter()
router.register("todo", TodoListViewSet, basename="todo")

urlpatterns = router.urls
