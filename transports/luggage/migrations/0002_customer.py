# Generated by Django 3.2.8 on 2021-12-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('mobile', models.IntegerField(max_length=25)),
                ('emailid', models.EmailField(max_length=225)),
                ('postcode', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('logo', models.ImageField(upload_to='productimg')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]