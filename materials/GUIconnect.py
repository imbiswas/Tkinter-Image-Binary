from materials import ColourImage,GreyScaleImage,BinaryImage

class GUI(object):
    def __init__(self,threshold,anotherlist):
        self.threshold=threshold
        self.anotherlist=anotherlist

    def processes(self):
        if len(self.anotherlist[1]) == 5:
            appendlists=[]
            avgthreshold=0
            for values in self.anotherlist:
                self.x = int(values[0])
                self.y = int(values[1])
                self.r = int(values[2])
                self.g = int(values[3])
                self.b = int(values[4])
                result = ColourImage.ColourImage(self.r, self.g, self.b)
                colorcode = result._determineColorValue()
                rbg=(self.r + self.g + self.b) / 3
                avgthreshold=avgthreshold+rbg
                if rbg < self.threshold:
                    output = 0
                else:
                    output = 1
                binaryimage = BinaryImage.BinaryImage(output)
                binaryoutput = binaryimage._determineColorValue()
                alist = [self.x, self.y,colorcode, binaryoutput]
                appendlists.append(alist)
            th=int(avgthreshold/len(appendlists))
            a = [th]

            return (appendlists, a)



        elif len(self.anotherlist[1]) == 3:
            appendlists = []
            avgthreshold = 0
            for values in self.anotherlist:
                self.x = int(values[0])
                self.y = int(values[1])
                self.v = int(values[2])
                result = GreyScaleImage.GreyScaleImage(self.v)
                colorcode = result._determineColorValue()
                avgthreshold = avgthreshold+self.v
                if self.v < self.threshold:
                    output = 0
                else:
                    output = 1
                binaryimage = BinaryImage.BinaryImage(output)
                binaryoutput = binaryimage._determineColorValue()
                alist = [self.x, self.y, colorcode, binaryoutput]
                appendlists.append(alist)
            th = int(avgthreshold / len(appendlists))
            a=[th]

            return (appendlists,a)
        else:
            print("Error Occured!!!")
