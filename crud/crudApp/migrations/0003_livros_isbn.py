# Generated by Django 5.1.7 on 2025-03-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0002_alter_livros_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='ISBN',
            field=models.IntegerField(default='0000000000000', max_length=13),
        ),
    ]
