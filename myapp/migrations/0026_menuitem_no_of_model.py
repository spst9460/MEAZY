# Generated by Django 4.1.7 on 2023-03-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_menuitem_no_of_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='no_of_model',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
