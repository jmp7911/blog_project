# Generated by Django 4.2.6 on 2023-10-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, unique=True, verbose_name='닉네임'),
        ),
    ]
