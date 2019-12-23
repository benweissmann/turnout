# Generated by Django 2.2.9 on 2019-12-18 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(primary_key=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(primary_key=True, default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multi_tenant.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
