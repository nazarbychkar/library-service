# Generated by Django 4.2.4 on 2023-08-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("borrowings", "0002_alter_borrowing_actual_return_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="actual_return_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]