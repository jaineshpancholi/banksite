# Generated by Django 3.1.4 on 2021-06-16 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0004_auto_20210608_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Hno',
            field=models.PositiveIntegerField(null=True),
        ),
    ]