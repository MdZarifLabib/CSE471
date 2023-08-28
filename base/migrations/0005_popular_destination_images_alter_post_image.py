# Generated by Django 4.2.4 on 2023-08-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_popular_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='popular_destination',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='destination_Images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_Images'),
        ),
    ]