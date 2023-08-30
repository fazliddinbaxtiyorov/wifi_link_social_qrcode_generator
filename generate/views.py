from django.shortcuts import render
import qrcode
from django.conf import settings
import wifi_qrcode_generator.generator
from . import forms


def wifi_qr_code(request):
    if request.method == 'POST':
        form = forms.WifiForm(request.POST)
        if form.is_valid():
            wifi_name = request.POST['wifi_name']
            encryption = request.POST['encryption']
            password = request.POST['password']
            qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
                ssid={wifi_name}, hidden=False, authentication_type='WPA', password={password}
            )
            img = qr_code.make_image()
            img_name = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + '/' + str(img_name)
            img.save(img_path)
            form.save()

            return render(request, 'generate/index.html', {'img_name': img_name, 'form': form})
    else:
        form = forms.WifiForm()

    return render(request, 'generate/index.html', {'form': form})


def link_qr_code(request):
    if request.method == 'POST':
        form = forms.LinkForm(request.POST)
        if form.is_valid():
            link = request.POST['link']
            link_code = qrcode.make(link)
            link_name = 'qr' + '.png'
            link_path = str(settings.MEDIA_ROOT) + '/' + str(link_name)
            link_code.save(link_path)
            form.save()

            return render(request, 'generate/link.html', {'form': form, 'img_name': link_name})
    else:
        form = forms.LinkForm()

    return render(request, 'generate/link.html', {'form': form})


def telegram(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://t.me/{username}"
            social = qrcode.make(url)
            social_name = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + '/' + str(social_name)
            social.save(img_path)

            return render(request, 'generate/social.html', {'form': form, 'img_name': social_name})
    else:
        form = forms.SocialForm()
    return render(request, 'generate/social.html', {'form': form})


def instagram(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST, request)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://instagram.com/{username}"
            social_name = qrcode.make(url)
            img_name = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + '/' + str(img_name)
            social_name.save(img_path)
            return render(request, 'generate/social.html', {'form': form, 'img_name': img_name})
    else:
        form = forms.SocialForm()
    return render(request, 'generate/social.html', {'form': form})


def twitter(request):
    if request.method == 'POST':
        form = forms.SocialForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            url = f"https://twitter.com/{username}"
            social_name = qrcode.make(url)
            img_name = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + '/' + str(img_name)
            social_name.save(img_path)
            return render(request, 'generate/social.html', {'form': form, 'img_name': img_name})
    else:
        form = forms.SocialForm()
    return render(request, 'generate/social.html', {'form': form})