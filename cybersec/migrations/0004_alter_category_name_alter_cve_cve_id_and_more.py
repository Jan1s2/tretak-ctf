# Generated by Django 5.0.6 on 2024-06-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybersec', '0003_alter_cve_cvss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cve',
            name='cve_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cwe',
            name='cwe_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='exploit',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='flag',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
