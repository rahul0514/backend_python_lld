# Generated by Django 5.0.6 on 2024-05-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomdemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
