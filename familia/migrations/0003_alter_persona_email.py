# Generated by Django 4.0.4 on 2022-05-31 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_persona_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]