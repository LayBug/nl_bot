# Generated by Django 3.1 on 2020-08-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20200822_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threadreplyjob',
            name='thread_uri',
        ),
    ]
