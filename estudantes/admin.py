from django.contrib import admin
from .models import ContatoEstudante, Estudante
# Register your models here.

class ContatoEstudanteInline(admin.StackedInline):
    model = ContatoEstudante
    fields = [
        'nome',
        'email',
        'telefone',
        'celular',
        'ativo',
        'observacoes',
    ]

    extra = 0

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'observacoes')

    inlines = [ContatoEstudanteInline]
