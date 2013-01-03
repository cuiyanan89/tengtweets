from django.http import HttpResponse

def home(request):
    import django
    info = str(django.VERSION)
    return HttpResponse(info)
