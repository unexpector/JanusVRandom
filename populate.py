import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gettingstarted.settings')

from hello.models import RandomSites


def populate():
    add_randomsite(sitename="Random Wordpress",
        src="http://en.blog.wordpress.com/next/")

    add_randomsite(sitename="Random Wikipedia",
        src="http://en.wikipedia.org/wiki/Special:Random")

    add_randomsite(sitename="Youtube Random Video",
        src="http://en.wikipedia.org/wiki/Special:Random")

    add_randomsite(sitename="Map Crunch",
        src="http://www.mapcrunch.com/")

    add_randomsite(sitename="Random Reddit",
        src="http://www.reddit.com/r/random")

    add_randomsite(sitename="Crakced",
        src="http://www.cracked.com/")

    add_randomsite(sitename="Random Imgur",
        src="http://imgur.com/random")

    add_randomsite(sitename="Random Spotify",
        src="http://www.karnhuset.net/demos/spotify/randomSong/")

    # Print out what we have added to the user.
    for p in RandomSites.objects.filter:
            print "- {0} - {1}".format(str(p))

def add_randomsite(sitename, src):
    p = RandomSites.objects.get_or_create(sitename=sitename, src=src)[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Unexpector population script..."
    populate()