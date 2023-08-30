from django.forms import ModelForm
from .models import WiFiQRCode, LinkQRCode, SocialMediaQRCode


class WifiForm(ModelForm):
    class Meta:
        model = WiFiQRCode
        fields = ['wifi_name', 'encryption', 'password']


class LinkForm(ModelForm):
    class Meta:
        model = LinkQRCode
        fields = ['link']


class SocialForm(ModelForm):
    class Meta:
        model = SocialMediaQRCode
        fields = ['username']




