# Generated by Django 2.2.5 on 2020-02-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petalWidth', models.ImageField(upload_to='')),
            ],
        ),
    ]
