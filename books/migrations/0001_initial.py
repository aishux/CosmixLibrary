# Generated by Django 3.1.7 on 2021-04-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addBook',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]