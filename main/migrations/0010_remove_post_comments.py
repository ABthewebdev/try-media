# Generated by Django 5.1.7 on 2025-03-14 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_comment_created_at_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
