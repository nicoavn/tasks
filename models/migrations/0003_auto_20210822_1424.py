# Generated by Django 3.2.6 on 2021-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20210822_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
