from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TodosViewSet

router = DefaultRouter()
# todos here referes to ../todos/.. -> todos resource base url that
# will be used to generate paths based on viewset actions
router.register(r"todos", TodosViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
