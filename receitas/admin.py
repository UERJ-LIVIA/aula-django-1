from django.contrib import admin

# Register your models here.
from .models import Medicamento, Receita

admin.site.register(Medicamento)
admin.site.register(Receita)