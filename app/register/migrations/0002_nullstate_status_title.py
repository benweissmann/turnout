# Generated by Django 2.2.10 on 2020-03-09 19:25

import common.enums
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=enumfields.fields.EnumField(default='Pending', enum=common.enums.TurnoutRegistrationStatus, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='title',
            field=enumfields.fields.EnumField(enum=common.enums.PersonTitle, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mailing_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registration_mailing', to='election.State'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='previous_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registration_previous', to='election.State'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registration_primary', to='election.State'),
        ),
    ]
