# Generated by Django 3.2.19 on 2023-11-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branches'),
        ),
    ]
