# Generated by Django 4.1.7 on 2023-05-06 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_orderbus_uploaded'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Uploaded',
        ),
        migrations.AddField(
            model_name='order',
            name='aadhar_card',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='order',
            name='driving_license',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='order',
            name='passport_photo',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
