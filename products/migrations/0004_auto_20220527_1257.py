# Generated by Django 3.2 on 2022-05-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_case_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='category',
            field=models.CharField(default='cpu', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='gpu',
            name='category',
            field=models.CharField(default='gpu', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='category',
            field=models.CharField(default='motherboard', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='ram',
            name='category',
            field=models.CharField(default='ram', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='storage',
            name='category',
            field=models.CharField(default='storage', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(default='case', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='psu',
            name='category',
            field=models.CharField(default='psu', editable=False, max_length=20),
        ),
    ]
