# Generated by Django 2.2.5 on 2019-09-30 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LBook', '0010_notify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='student',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='book',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='issueBook',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='student',
        ),
        migrations.DeleteModel(
            name='Registers',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='IssueBook',
        ),
        migrations.DeleteModel(
            name='Notify',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
