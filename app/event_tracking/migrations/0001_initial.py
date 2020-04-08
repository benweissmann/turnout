# Generated by Django 2.2.12 on 2020-04-06 19:18

import common.enums
from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('action', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', django_smalluuid.models.SmallUUIDField(default=django_smalluuid.models.UUIDDefault(), editable=False, primary_key=True, serialize=False, unique=True)),
                ('event_type', enumfields.fields.EnumField(enum=common.enums.EventType, max_length=100)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Action')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]