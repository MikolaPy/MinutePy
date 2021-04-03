# Generated by Django 3.1.7 on 2021-04-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40, verbose_name='tags name')),
            ],
            options={
                'verbose_name': 'teg',
                'verbose_name_plural': 'tegs',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='sobject'),
        ),
    ]
