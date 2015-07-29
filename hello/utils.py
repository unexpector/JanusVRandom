from random import randint

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

    def addtodict(self):
        updatedict = context_dict.update({'newvalue': self.newobjx})
        return updatedict


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