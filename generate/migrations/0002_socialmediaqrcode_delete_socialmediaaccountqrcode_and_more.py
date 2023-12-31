# Generated by Django 4.0.3 on 2023-08-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaQRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='SocialMediaAccountQRCode',
        ),
        migrations.AlterField(
            model_name='wifiqrcode',
            name='encryption',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='wifiqrcode',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='wifiqrcode',
            name='wifi_name',
            field=models.CharField(max_length=60),
        ),
    ]
