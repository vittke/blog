# Generated by Django 4.1 on 2022-09-09 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='post',
        ),
    ]
