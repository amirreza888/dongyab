# Generated by Django 3.1.5 on 2021-01-11 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210111_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_owner',
        ),
        migrations.AddField(
            model_name='factor',
            name='factor_member_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.group'),
            preserve_default=False,
        ),
    ]
