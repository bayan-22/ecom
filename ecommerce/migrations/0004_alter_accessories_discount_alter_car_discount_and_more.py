# Generated by Django 4.1.7 on 2023-03-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_accessories_price_after_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='discount',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='car',
            name='discount',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='carparts',
            name='discount',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]