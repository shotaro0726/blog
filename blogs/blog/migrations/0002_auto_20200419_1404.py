# Generated by Django 2.2.6 on 2020-04-19 05:04

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
    ]
