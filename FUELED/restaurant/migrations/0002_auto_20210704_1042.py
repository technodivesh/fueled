# Generated by Django 3.2.4 on 2021-07-04 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('restaurant', 'review')},
        ),
    ]
