# Generated by Django 3.0.2 on 2020-06-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_car_name', models.CharField(blank=True, max_length=33, null=True)),
                ('take_realtor', models.CharField(blank=True, max_length=20, null=True)),
                ('take_customer', models.CharField(blank=True, max_length=20, null=True)),
                ('take_message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
