# Generated by Django 3.2.2 on 2021-05-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='film_url',
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
