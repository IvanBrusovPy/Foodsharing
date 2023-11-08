# Generated by Django 4.2.5 on 2023-10-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_service', '0005_alter_offer_quantity_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='In process', max_length=20),
        ),
    ]
