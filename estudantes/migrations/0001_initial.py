# Generated by Django 3.0.8 on 2020-07-07 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Pessoa')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Estudante',
                'verbose_name_plural': 'Estudantes',
            },
            bases=('core.pessoa',),
        ),
        migrations.CreateModel(
            name='ContatoEstudante',
            fields=[
                ('contato_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Contato')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudantes.Estudante', verbose_name='Estudante')),
            ],
            options={
                'verbose_name': 'Contato de Estudante',
                'verbose_name_plural': 'Contatos de Estudantes',
            },
            bases=('core.contato',),
        ),
    ]
