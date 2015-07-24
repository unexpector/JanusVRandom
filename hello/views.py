from django.shortcuts import render
from django.http import HttpResponse
from hello.models import RandomSites, ObjectLibrary, Rooms
from random import randint
from hello.forms import ObjectForm
from numpy import array

# Create your views here.
def index(request):
    namepicked = "Random Imgur"
    reddit="Random Reddit"
    wikipedia="Random Wikipedia"
    random_list = RandomSites.objects.get(sitename=namepicked).src
    randomreddit = RandomSites.objects.get(sitename=reddit).src
    randomwikipedia = RandomSites.objects.get(sitename=wikipedia).src
    wikipedia_id=  RandomSites.objects.get(sitename=wikipedia).id
    thenumber = randint(1, 26)
    fullrandom = RandomSites.objects.get(id=thenumber).src
    newarray = [2,3,1]
    x_dimension = newarray[0]
    y_dimension = newarray[1]
    z_dimension = newarray[2]
    roomrandom = randint(1, 14)
    random_room = Rooms.objects.get(id=roomrandom).localasset
    random_model ="Subwoofer"
    themodel = ObjectLibrary.objects.get(objectname=random_model).src
    context_dict = {'boldmessage': random_list, 'randomreddit': randomreddit, 'randomwikipedia': randomwikipedia, 'thenumber': thenumber, 'themodel': themodel, 'wikipediaid': wikipedia_id, 'realrandom': fullrandom, 'randomroom': random_room, 'xvalue': x_dimension, 'yvalue': y_dimension, 'zvalue': z_dimension }
    context_dict['page_name'] = "this is the page name"
    return render(request, 'unexpector-template.html', context_dict)


def db(request):

    greetings = "hello"

    return render(request, 'db.html', {'greetings': greetings})

def about(request):
    pagetext = "<html><body> Here is the link to the main page</body></html>"

    return HttpResponse(pagetext)

def category(request, site_name_slug):

    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        site = RandomSites.objects.get(sitename=site_name_slug)
        context_dict['site_name'] = site

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        url = RandomSites.objects.get(sitename=site).src

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

def add_object(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = ObjectForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ObjectForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'add_forms.html', {'form': form})
