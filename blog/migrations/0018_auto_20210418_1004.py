# Generated by Django 3.1.7 on 2021-04-18 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210418_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='contetn_type',
            new_name='content_type',
        ),
    ]
