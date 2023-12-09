# Generated by Django 4.2.4 on 2023-08-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bayur', '0009_rename_listing_data_listing_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing_product',
            name='Seller_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_bayur.seller_user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing_product',
            name='Listing_immage',
            field=models.FileField(default='/abc.jpg', upload_to='Listing/'),
        ),
    ]