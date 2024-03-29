# Generated by Django 3.2.19 on 2023-11-20 09:28

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('contact', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('branch', models.IntegerField()),
                ('answer1', models.CharField(max_length=120)),
            ],
        ),
    ]
