# Generated by Django 4.0.3 on 2022-03-28 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Narration', models.CharField(blank=True, max_length=500, null=True)),
                ('Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.expensename')),
            ],
        ),
    ]
