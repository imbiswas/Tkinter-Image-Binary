
class GreyScaleImage(object):
    def __init__(self, v):
        self.v=v

    def _determineColorValue(self):
        return ("#%02x%02x%02x" % (self.v, self.v, self.v))