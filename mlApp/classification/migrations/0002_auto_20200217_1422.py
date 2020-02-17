# Generated by Django 2.2.5 on 2020-02-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_file',
            name='petalWidth',
        ),
        migrations.AddField(
            model_name='image_file',
            name='image',
            field=models.ImageField(null=True, upload_to='uploaded_pic'),
        ),
        migrations.AddField(
            model_name='image_file',
            name='url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
