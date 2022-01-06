# Generated by Django 3.2.9 on 2022-01-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_twitter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Facebook_URL',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Instagram_ID',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='TikTok_ID',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
