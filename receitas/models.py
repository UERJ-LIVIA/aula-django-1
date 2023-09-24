from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

import datetime

# Create your models here.
class Medicamento(models.Model):

    class Unidade(models.TextChoices):
        ML = "ML", _("Milímetro")
        COMP = "COMP", _("Comprimido")

    nome        = models.TextField()
    dose        = models.IntegerField()
    unidade     = models.CharField(max_length=150, choices=Unidade.choices, default=Unidade.ML)
    pub_date    = models.DateTimeField(default=datetime.datetime.now)


class Receita(models.Model):

    paciente     = models.ForeignKey(User, on_delete=models.CASCADE, related_name="paciente")
    medico       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medico")
    medicamento  = models.ManyToManyField(Medicamento)
    pub_date     = models.DateTimeField(default=datetime.datetime.now)