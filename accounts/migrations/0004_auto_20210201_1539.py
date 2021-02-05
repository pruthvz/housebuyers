# Generated by Django 3.1.5 on 2021-02-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='buyer_number',
            field=models.BigIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='buyer_solicitor_name',
            field=models.CharField(default=2, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='household_income',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]