from django.http import HttpResponse
from django.views.generic import TemplateView


def hellofunction(request):
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject


class helloClass(TemplateView):
    template_name = 'hello.html'
