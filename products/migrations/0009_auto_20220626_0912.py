# Generated by Django 3.2 on 2022-06-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220626_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='case',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='psu',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='psu',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='ram',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='storage',
            name='total_score',
        ),
    ]
