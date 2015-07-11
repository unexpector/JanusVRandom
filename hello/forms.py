from django import forms
from hello.models import ObjectLibrary, RandomSites

class ObjectForm(forms.ModelForm):
    objectname = forms.CharField(max_length=128, help_text="Please enter the object name")
    idseed= forms.CharField(max_length=128, help_text="Please enter the ID Seed")
    src = forms.CharField(max_length=128, help_text="Please enter the URL")
    txtsrc = forms.CharField(max_length=128, help_text="Please enter texture source")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = ObjectLibrary
        fields = ('objectname',)


class RandomSitesForm(forms.ModelForm):
    sitename = forms.CharField(max_length=128, help_text="Please enter the Site Name")
    src = forms.CharField(max_length=128, help_text="Please enter the URL of the page")


    class Meta:
        # Provide an association between the ModelForm and a model
        model = RandomSites

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('src',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')