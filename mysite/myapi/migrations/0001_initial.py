# Generated by Django 4.2.7 on 2023-11-17 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finanzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
