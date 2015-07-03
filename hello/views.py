from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    newvalue = "new value"

    return render(request, 'unexpector-template.html', {'greetings': newvalue})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def about(request):
    pagetext = "<html><body> <a href="https://obscure-cliffs-2136.herokuapp.com/">Here is the link to the main page</a></body></html>"
    return HttpResponse(pagetext)

