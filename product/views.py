from django.http import HttpResponse
from .models  import Tea
from django.template import loader


def index(request):
    tea= Tea.objects.all()
    template = loader.get_template('product/index.html')
    context = {
        'tea': tea
    }
    return HttpResponse(template.render(context,request))


def detail(request,Name):
    tea1 = Tea.objects.get(name=Name)
    template = loader.get_template('product/detail.html')
    context = {
        'tea1':tea1
    }
    return HttpResponse(template.render(context,request))