# Generated by Django 4.2.16 on 2024-10-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_aboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
