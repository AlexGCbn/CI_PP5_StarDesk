# Generated by Django 3.2 on 2022-06-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220624_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealcase',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealcpu',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealgpu',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealmotherboard',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealpsu',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealram',
            name='price_was',
        ),
        migrations.RemoveField(
            model_name='dealstorage',
            name='price_was',
        ),
    ]