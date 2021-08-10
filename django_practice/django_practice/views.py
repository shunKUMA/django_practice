from django.http import HttpResponse


def hellofunction(request):
    return HttpResponse('<h1>hello world</h1>')
