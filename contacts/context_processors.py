from django.conf import settings


def default_picture(request):
    return {
        'default_picture' : f'{settings.STATIC_URL}img/default_picture.jpg'
    }