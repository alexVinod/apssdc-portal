# Generated by Django 2.2.5 on 2019-09-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LBook', '0011_auto_20190930_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]