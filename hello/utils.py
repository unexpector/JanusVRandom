from random import randint

import urllib2
import json

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
        clientID = '9aa094141cc554a'
        req = urllib2.urlopen('https://api.imgur.com/3/gallery/random/random/1')
        req.add_header('Authorization', 'Client-ID ' + clientID)
        response = urllib2.urlopen(req)
        response = json.loads(response.read())
        return str(response[u'data'][u'link'])







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