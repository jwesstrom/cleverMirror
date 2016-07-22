class transformProperties(object):
    def __innit__(self, posX, posY, red, green, blue, sizeX, sixeY, rot, angleStart, angleEnd):
        self.posX = posX
        self.posY = posY
        self.red = red
        self.green = green
        self.blue = blue
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.rot = root
        self.angleStart = angleStart
        self.angleEnd = angleEnd

    def pos(self, posX, posY):
        pos = [posX, posY]
        return pos

    def size(self, sizeX, sizeY):
        self.size = [sizeX, sizeY]
        return self.size


test = transformProperties()
test.pos = [10, 15]

print test.pos


# def __innit__(self, posX, posY, red, green, blue, sizeX, sixeY, rot, angleStart, angleEnd):
