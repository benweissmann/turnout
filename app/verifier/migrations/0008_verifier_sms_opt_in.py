# Generated by Django 2.2.11 on 2020-04-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifier', '0007_lookup_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookup',
            name='sms_opt_in',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

