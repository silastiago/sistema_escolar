from django.contrib import admin
from .models import ContatoEstudante, Estudante
from disciplinas.models import Disciplina
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

class DisciplinaInline(admin.StackedInline):
    model = Disciplina
    fields = [
        'nome',
        'nota1',
        'nota2',
        'nota3',
        'nota4',
        'observacoes',
    ]

    extra = 0


@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'observacoes')

    inlines = [ContatoEstudanteInline, DisciplinaInline]
