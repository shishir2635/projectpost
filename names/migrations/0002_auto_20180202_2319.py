# Generated by Django 2.0.1 on 2018-02-02 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='names',
            new_name='name',
        ),
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
    ]
