from django.urls import path

from .views import testeAPIView, testeDoisAPIView, UserAPIView, UserCreateAPIView, ProfileAPIView

urlpatterns = [
    path('', testeAPIView.as_view()),
    path('dois/', testeDoisAPIView.as_view()),
    path('usuarios/', UserAPIView.as_view()),
    path('usuarios/create/', UserCreateAPIView.as_view()),
    path('profiles/', ProfileAPIView.as_view()),
    path('profiles/<pk>/', ProfileAPIView.as_view()),
]