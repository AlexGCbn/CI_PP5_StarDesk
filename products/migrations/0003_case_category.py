# Generated by Django 3.2 on 2022-05-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220526_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.CharField(blank=True, default='case', max_length=20, null=True),
        ),
    ]
