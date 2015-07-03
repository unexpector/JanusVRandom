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
    pagetext = "<html><body> Here is the link to the main page</body></html>"
    return HttpResponse(pagetext)

