# Generated by Django 5.0 on 2024-10-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_followers_delete_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]