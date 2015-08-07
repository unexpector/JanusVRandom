from random import randint
import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class makeobject(object):
    def __init__(self, name):
        self.name = name
        self.position = []    # creates a new location list
        self.newobjx = 1
        self.newobjy= 1
        self.newobjz= 1

    def add_co_ords(self, location):
        self.position.append(location)

    def setcords(self, xpos,ypos,zpos):
        self.newobjx = xpos
        self.newobjy = ypos
        self.newobjz = zpos

    def randcords(self):
        setx = randint(-2, 5)
        sety = 1
        setz = randint(-10,-1)
        objlocation = [setx,sety,setz]
        #Set Dimensions
        self.newobjx = objlocation[0]
        self.newobjy = objlocation[1]
        self.newobjz = objlocation[2]

    def addtodict(self, dictionary):
        self.xvar = "x"
        self.yvar = "y"
        self.zvar = "z"
        self.xname = self.name + self.xvar
        self.yname = self.name + self.yvar
        self.zname = self.name + self.zvar
        xdict = {self.xname: self.newobjx,self.yname: self.newobjy, self.zname: self.newobjz }

        updatedict = dictionary.update(xdict)

        return updatedict, self.xname

class imgur(object):
    def __init__(self, name):
        self.name = name

    def takeinput(self):
        json1_file = open('https://api.imgur.com/3/gallery/random/random/1')
        json1_str = json1_file.read()
        json1_data = json.loads(json1_str)[0]


def newobject():
    setx = randint(-2, 5)
    sety = 1
    setz = randint(-10,-1)
    objlocation = [setx,sety,setz]
    #Set Dimensions
    newobjx = objlocation[0]
    newobjy = objlocation[1]
    newobjz = objlocation[2]
    return newobjx, newobjy, newobjz