from django.db import models
from core.models import Pessoa

class Estudante(Pessoa):
    """
    Classe Estudante implementa as funções relacionadas a um estudante da plataforma.
    """
    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True
    )

    class Meta:
        app_label = "estudantes"
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

