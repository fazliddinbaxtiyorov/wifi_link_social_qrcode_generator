from django.db import models


class WiFiQRCode(models.Model):
    wifi_name = models.CharField(max_length=60)
    encryption = models.CharField(max_length=5)
    password = models.CharField(max_length=40)


class LinkQRCode(models.Model):
    link = models.URLField()


class SocialMediaQRCode(models.Model):
    username = models.CharField(max_length=80)
