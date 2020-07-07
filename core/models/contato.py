from django.db import models

class Contato(models.Model):
    """
    Classe Contato implementa as funções relacionadas a um contato de uma pessoa na plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    email = models.EmailField(
        max_length=200,
        verbose_name="E-mail",
        blank=True
    )

    telefone = models.CharField(
        max_length=30,
        verbose_name="Telefone",
        blank=True
    )

    celular = models.CharField(
        max_length=30,
        verbose_name="Celular",
        blank=True
    )

    ativo = models.BooleanField(
        verbose_name="Ativo",
        default=True
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

