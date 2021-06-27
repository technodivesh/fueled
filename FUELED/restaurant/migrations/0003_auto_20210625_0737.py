# Generated by Django 3.2.4 on 2021-06-25 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_thumbdown_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='locality',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Area Name'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant.restaurant'),
        ),
    ]