# Generated by Django 3.1.7 on 2021-03-05 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210305_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='speakers',
            new_name='faculty',
        ),
    ]