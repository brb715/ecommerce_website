# Generated by Django 4.0.6 on 2022-11-03 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_product_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serie',
            options={'ordering': ['-date']},
        ),
    ]
