# Generated by Django 4.2.6 on 2023-10-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='account/$<django.db.models.fields.CharField>/'),
        ),
    ]
