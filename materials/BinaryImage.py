class BinaryImage(object):
    def __init__(self,b):
        self.b=b

    def _determineColorValue(self):
            v = 255*self.b
            return ("#%02x%02x%02x" % (v, v, v))
