# Generated by Django 5.0.6 on 2024-06-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coinflip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('T', 'Tail'), ('H', 'Head')], max_length=1)),
                ('flip_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
