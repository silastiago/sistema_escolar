from django.db import models
from estudantes.models import Estudante

class Disciplina(models.Model):
    """
    Classe Disciplina implementa as funções relacionadas a uma disciplina da plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    nota1 = models.FloatField(
        verbose_name="Nota1"
    )

    nota2 = models.FloatField(
        verbose_name="Nota2"
    )

    nota3 = models.FloatField(
        verbose_name="Nota3"
    )

    nota4 = models.FloatField(
        verbose_name="Nota4"
    )

    estudante = models.ForeignKey(
        Estudante,
        verbose_name="Estudante",
        on_delete=models.CASCADE
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True
    )

    @property
    def aprovado(self):

        valor =  (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4
        if( valor > 7):
            return 'REPROVADO'
        else:
            return 'APROVADO'


    class Meta:
        app_label = "disciplinas"
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

