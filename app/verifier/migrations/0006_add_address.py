# Generated by Django 2.2.10 on 2020-02-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifier', '0005_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookup',
            name='address1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lookup',
            name='address2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
