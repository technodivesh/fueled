# Generated by Django 3.2.4 on 2021-07-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fldUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='unique alphanumeric identifier', max_length=30, unique=True),
        ),
    ]
