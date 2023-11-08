# Generated by Django 4.2.5 on 2023-10-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_service', '0002_remove_cafe_description_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='available',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BinaryField(default=False, null=True),
        ),
    ]
