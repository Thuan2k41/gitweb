# Generated by Django 5.0 on 2024-10-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0009_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(default='Math', max_length=50),
        ),
    ]