# Generated by Django 4.2.11 on 2024-04-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotels",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=500)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
            ],
        ),
    ]
