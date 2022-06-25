# Generated by Django 3.2 on 2022-06-25 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20220625_1208'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.storage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RamReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ram')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PsuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.psu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MotherboardReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.motherboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GpuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.gpu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CpuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cpu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CaseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=3)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.case')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
