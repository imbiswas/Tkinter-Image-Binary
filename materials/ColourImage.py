class ColourImage(object):
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    def _determineColorValue(self):
        return str("#%02x%02x%02x" % (self.r, self.g, self.b))
        # return ("hello")


