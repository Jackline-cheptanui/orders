# Generated by Django 3.2.8 on 2021-10-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generateorder', '0002_alter_generateorder_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generateorder',
            name='category',
            field=models.CharField(choices=[('1', 'vegetable'), ('2', 'dry goods'), ('3', 'others')], max_length=4, null=True),
        ),
    ]
