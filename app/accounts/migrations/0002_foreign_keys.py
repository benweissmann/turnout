# Generated by Django 2.2.9 on 2019-12-18 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('multi_tenant', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='active_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='active_client', to='multi_tenant.Client'),
        ),
        migrations.AddField(
            model_name='user',
            name='clients',
            field=models.ManyToManyField(through='multi_tenant.Association', to='multi_tenant.Client'),
        ),
    ]
