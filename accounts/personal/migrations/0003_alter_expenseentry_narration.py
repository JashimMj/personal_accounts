# Generated by Django 4.0.3 on 2022-03-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_expensename_expenseentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseentry',
            name='Narration',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
