from django.shortcuts import render, HttpResponse

# Create your views here.


def index_page(request):
    return HttpResponse("<h1>Muna Darling</h1>")


def greet(request, name):
    return render(request, 'hello/greet.html', {
        "name": name.title()
    })
