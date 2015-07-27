from random import randint

class makeobject(object):
    def __init__(self, name):
        self.name = name
        self.position = []    # creates a new location list

    def add_co_ords(self, location):
        self.position.append(location)

    def setcords(self, xpos,ypos,zpos):
        newobjx = xpos
        newobjy = ypos
        newobjz = zpos


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