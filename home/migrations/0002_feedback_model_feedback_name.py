# Generated by Django 3.0.5 on 2020-08-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='model_feedback_name',
            field=models.CharField(default='Name not provided', max_length=30),
        ),
    ]