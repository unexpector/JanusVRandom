class item(object):
    def createitem(self):
        setx = randint(-2, 5)
        sety = 1
        setz = randint(-10,-1)
        objlocation = [setx,sety,setz]
        #Set Dimensions
        objx = objlocation[0]
        objy = objlocation[1]
        objz = objlocation[2]

def newobject(name):
    setx = randint(-2, 5)
    sety = 1
    setz = randint(-10,-1)
    objlocation = [setx,sety,setz]
    #Set Dimensions
    objx = objlocation[0]
    objy = objlocation[1]
    objz = objlocation[2]
    return objx,objy,objz