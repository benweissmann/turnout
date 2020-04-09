# Generated by Django 2.2.12 on 2020-04-09 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.IntegerField(primary_key=True, serialize=False)),
                ('external_updated', models.DateTimeField(null=True)),
                ('hours', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.IntegerField(primary_key=True, serialize=False)),
                ('external_updated', models.DateTimeField(null=True)),
                ('title', models.TextField(null=True)),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='official.Office')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.IntegerField(primary_key=True, serialize=False)),
                ('external_updated', models.DateTimeField(null=True)),
                ('city', models.TextField(null=True)),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='official.Office')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
