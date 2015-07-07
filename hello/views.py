from django.shortcuts import render
from django.http import HttpResponse
from hello.models import RandomSites, ObjectLibrary, Rooms


# Create your views here.
def index(request):
    newvalue = "new value"
    namepicked = "twitter"
    random_list = RandomSites.objects.('src').filter(sitename=namepicked).order_by('src')
    context_dict = {'boldmessage': random_list}

    return render(request, 'unexpector-template.html', context_dict)


def db(request):

    greetings = "hello"

    return render(request, 'db.html', {'greetings': greetings})

def about(request):
    pagetext = "<html><body> Here is the link to the main page</body></html>"
    return HttpResponse(pagetext)

