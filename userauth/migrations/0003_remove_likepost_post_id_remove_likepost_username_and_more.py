# Generated by Django 5.1.1 on 2024-11-20 04:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

def migrate_data(apps,schema_editor):
    LikePost = apps.get_model('userauth','LikePost')
    Post = apps.get_model('userauth', 'Post')
    User = apps.get_model('auth', 'User')

    for lp in LikePost.objects.all():
        try:
            post = Post.objects.get(id=lp.old_post_id)
            user = User.objects.get(username=lp.old_username)
            lp.post = post
            lp.user = user
            lp.save()
        except (Post.DoesNotExist, User.DoesNotExist):
            continue

class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_likecomment_comment_no_of_likes_alter_post_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='likepost',
            old_name='post_id',
            new_name='old_post_id',
        ),
        migrations.RenameField(
            model_name='likepost',
            old_name='username',
            new_name='old_username',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
        migrations.AddField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.post'),
        ),
        migrations.AddField(
            model_name='likepost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.RunPython(migrate_data),
        migrations.RemoveField(
            model_name='likepost',
            name='old_post_id',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='old_username',
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
