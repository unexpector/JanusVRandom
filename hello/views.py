from django.shortcuts import render
from django.http import HttpResponse
from hello.models import RandomSites, ObjectLibrary, Rooms
from random import randint

# Create your views here.
def index(request):
    namepicked = "Random Imgur"
    reddit="Random Reddit"
    wikipedia="Random Wikipedia"
    random_list = RandomSites.objects.get(sitename=namepicked).src
    randomreddit = RandomSites.objects.get(sitename=reddit).src
    randomwikipedia = RandomSites.objects.get(sitename=wikipedia).src
    wikipedia_id=  RandomSites.objects.get(sitename=wikipedia).id
    thenumber = randint(1, 10)
    fullrandom = RandomSites.objects.get(id=thenumber).src
    random_model ="Subwoofer"
    themodel = ObjectLibrary.objects.get(objectname=random_model).src
    context_dict = {'boldmessage': random_list, 'randomreddit': randomreddit, 'randomwikipedia': randomwikipedia, 'thenumber': thenumber, 'themodel': themodel, 'wikipediaid': wikipedia_id, 'realrandom': fullrandom }
    context_dict['page_name'] = "this is the page name"
    return render(request, 'unexpector-template.html', context_dict)


def db(request):

    greetings = "hello"

    return render(request, 'db.html', {'greetings': greetings})

def about(request):
    pagetext = "<html><body> Here is the link to the main page</body></html>"
    return HttpResponse(pagetext)

