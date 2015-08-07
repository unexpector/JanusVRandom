from django.shortcuts import render
from django.http import HttpResponse
from hello.models import RandomSites, ObjectLibrary, Rooms
from random import randint
from hello.forms import ObjectForm
from hello.utils import newobject, makeobject, imgur
import scrapy
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

    #Set Number Of Cubes
    #cubeamount = randint(1,4)
    #for each in cubeamount


    #Room Random Code
    roomrandom = randint(1, 14)
    random_room = Rooms.objects.get(id=roomrandom).localasset
    random_model ="Subwoofer"

    object_one = makeobject('object_one')
    object_one.randcords()
    object_two = makeobject('object_two')
    object_two.randcords()
    object_three = makeobject('object_three')
    object_three.randcords()

    jsontest = []
    imgur1 = imgur(imgurone)
    imgurone.takeinput(jsontest)


    themodel = ObjectLibrary.objects.get(objectname=random_model).src
    context_dict = {'boldmessage': object_one.newobjx, 'randomreddit': randomreddit, 'randomwikipedia': randomwikipedia, 'thenumber': thenumber, 'themodel': themodel, 'wikipediaid': wikipedia_id, 'realrandom': fullrandom, 'randomroom': random_room, 'one_xvalue': object_one.newobjx, 'one_yvalue': object_one.newobjy, 'one_zvalue': object_one.newobjz, 'jsontest': jsontest}
    context_dict['page_name'] = "this is the page name"
    #context_dict.update({'newvalue': thecube.newobjx})
    object_one.addtodict(context_dict)
    object_two.addtodict(context_dict)
    object_three.addtodict(context_dict)
    context_dict['xname'] = object_one.xname
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
