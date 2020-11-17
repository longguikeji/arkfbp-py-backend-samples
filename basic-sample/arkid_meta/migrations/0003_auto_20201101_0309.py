# Generated by Django 3.1.2 on 2020-11-01 03:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('arkid_meta', '0002_auto_20201030_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='WechatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('wechat_user_id', models.CharField(blank=True, max_length=255, verbose_name='Github ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='githubuser',
            name='wechat_user',
            field=models.OneToOneField(default=123, on_delete=django.db.models.deletion.PROTECT, related_name='wechat_github_user', to='arkid_meta.wechatuser', verbose_name='微信用户'),
            preserve_default=False,
        ),
    ]
