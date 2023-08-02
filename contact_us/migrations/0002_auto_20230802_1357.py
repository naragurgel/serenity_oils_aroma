# Generated by Django 3.2.20 on 2023-08-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
