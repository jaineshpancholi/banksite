# Generated by Django 3.1.4 on 2021-06-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0007_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SenderName', models.CharField(max_length=100, null=True)),
                ('ReceiverName', models.CharField(max_length=100, null=True)),
                ('Amount', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
            ],
        ),
    ]