from django.urls import path, include
from rest_framework import routers

from . import views_api

api_router = routers.DefaultRouter()

api_router.register('users', views_api.UserViewSet)
api_router.register('questions', views_api.QuestionViewSet)
api_router.register('quizes', views_api.QuizViewSet)
urlpatterns = [
    path('api/', include(api_router.urls)),
    path('', include(api_router.urls)),
    path('', include(api_router.urls))
]