from django.urls import path

from .views import MedicamentosAPIView, MedicamentosPKAPIView, ReceitasAPIView, ReceitasCreateAPIView, ReceitasPKAPIView

urlpatterns = [
    path('medicamentos/', MedicamentosAPIView.as_view()),
    path('medicamentos/<pk>/', MedicamentosPKAPIView.as_view()),
    path('', ReceitasAPIView.as_view()),
    path('create/', ReceitasCreateAPIView.as_view()),
    path('<pk>/', ReceitasPKAPIView.as_view()),
]