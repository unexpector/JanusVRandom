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

def category(request, site_name_slug):

    ontext_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        site = RandomSites.objects.get(sitename=site_name_slug)
        context_dict['site_name'] = site

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        url = RandomSites.objects.filter(category=site)

        # Adds our results list to the template context under name pages.
        context_dict['src'] = url
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['sitename'] = site
    except RandomSites.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'showsites.html', context_dict)