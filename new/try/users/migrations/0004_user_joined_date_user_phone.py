# Generated by Django 4.2.1 on 2023-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]