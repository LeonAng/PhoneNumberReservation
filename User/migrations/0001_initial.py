# Generated by Django 2.0.4 on 2018-05-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pass_word', models.CharField(max_length=128)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField(default=0)),
            ],
        ),
    ]
