
from django.db import models
from core.models import Contato
from .estudante import Estudante

class ContatoEstudante(Contato):
    """
    Classe Contato implementa as funções relacionadas a um contato de um estudante na plataforma.
    """

    estudante = models.ForeignKey(
        Estudante,
        verbose_name="Estudante",
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = "estudantes"
        verbose_name = "Contato de Estudante"
        verbose_name_plural = "Contatos de Estudantes"

