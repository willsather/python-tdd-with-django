# Generated by Django 4.1.6 on 2023-02-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penguin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('island', models.CharField(max_length=50)),
                ('body_mass', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
