# Generated by Django 2.0.5 on 2018-06-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryManagement', '0010_auto_20180624_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='location',
            field=models.CharField(default='smc', max_length=50),
            preserve_default=False,
        ),
    ]