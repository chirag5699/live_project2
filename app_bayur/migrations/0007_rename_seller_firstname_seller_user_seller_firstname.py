# Generated by Django 4.2.4 on 2023-08-22 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_bayur', '0006_seller_user_alter_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_user',
            old_name='seller_firstname',
            new_name='Seller_firstname',
        ),
    ]
