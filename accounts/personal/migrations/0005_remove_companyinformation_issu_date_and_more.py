# Generated by Django 4.0.3 on 2022-03-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_cashreceive_cashreceiveentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinformation',
            name='issu_date',
        ),
        migrations.AddField(
            model_name='cashreceive',
            name='datess',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cashreceiveentry',
            name='To_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cashreceiveentry',
            name='datess',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='expenseentry',
            name='To_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expenseentry',
            name='datess',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='expensename',
            name='datess',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]