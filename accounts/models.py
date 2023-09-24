from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Perfil(models.Model):

    class Categoria(models.TextChoices):
        PACIENTE = "PACIENTE", _("Paciente")
        MEDICO = "MEDICO", _("Médico")
        # VARIAVEL INTERNA DA CLASSE - VALOR A SER REPASSADO - VALOR A SER EXPOSTO

    usuario     = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    nome        = models.TextField()
    categoria   = models.CharField(max_length=150, choices=Categoria.choices, default=Categoria.PACIENTE)
