# Generated by Django 3.1.7 on 2021-04-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210404_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tegs',
            field=models.ManyToManyField(to='blog.Teg'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='sobject'),
        ),
    ]
