# Generated by Django 4.0.6 on 2022-10-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_checkout_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]