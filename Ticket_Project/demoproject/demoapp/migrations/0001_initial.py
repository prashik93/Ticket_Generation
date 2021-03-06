# Generated by Django 4.0.3 on 2022-03-07 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=32)),
                ('category', models.CharField(choices=[('Travelling', 'Travelling'), ('Movie', 'Movie'), ('Tourism', 'Tourism')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked')], max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
