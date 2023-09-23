from django.urls import path

from .views import cadastro_view, login_view, logout_view

urlpatterns = [
    path('cadastro/', cadastro_view, name="cadastro_view"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
]