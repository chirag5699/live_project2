# Generated by Django 4.2.4 on 2023-09-09 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bayur', '0014_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_user',
            name='Seller_image',
            field=models.FileField(default='media/abc.jpg', upload_to='media/'),
        ),
        migrations.CreateModel(
            name='CheckoutDetals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('mobile_no', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=1000)),
                ('address2', models.CharField(max_length=1000)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('ZIPCode', models.IntegerField(default=0)),
                ('order_id', models.CharField(max_length=50)),
                ('bayer_detials', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bayur.user')),
            ],
        ),
    ]