# Generated by Django 3.1.5 on 2021-01-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210111_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factor',
            old_name='factor_member_group',
            new_name='factor_group',
        ),
    ]
