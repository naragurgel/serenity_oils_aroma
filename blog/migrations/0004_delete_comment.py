# Generated by Django 3.2.20 on 2023-08-21 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_favorites'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
