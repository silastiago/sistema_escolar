# Generated by Django 3.0.8 on 2020-07-07 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='user',
        ),
    ]