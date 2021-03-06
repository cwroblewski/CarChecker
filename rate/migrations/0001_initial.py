# Generated by Django 3.0.3 on 2020-11-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Very good')], verbose_name='users rate')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
