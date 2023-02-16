# Generated by Django 4.1.6 on 2023-02-16 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penguins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penguin',
            name='body_mass',
        ),
        migrations.RemoveField(
            model_name='penguin',
            name='gender',
        ),
        migrations.AddField(
            model_name='penguin',
            name='bill_depth_mm',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='penguin',
            name='bill_length_mm',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='penguin',
            name='body_mass_g',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='penguin',
            name='flipper_length_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='penguin',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('NA', 'Na')], default='NA', max_length=6),
        ),
    ]
