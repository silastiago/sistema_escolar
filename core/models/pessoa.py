
from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    """
    Classe Pessoa implementa as funções relacionadas a uma pessoa da plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome",
        help_text="Campo Obrigatório*"
    )

    cpf = models.CharField(
        max_length=18,
        verbose_name="CPF",
        unique=True,
        help_text="Campo Obrigatório*"
    )

    rg = models.CharField(
        max_length=30,
        verbose_name="RG",
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=150,
        verbose_name="Email",
        help_text="Campo Obrigatório*"
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
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

