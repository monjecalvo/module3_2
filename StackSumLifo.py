import StackLifo

class StackSumLifo(StackLifo.StackLifo):

    def __init__(self):
        super().__init__()
        self.__sum = 0

    def getSum(self):
        
        return self.__sum    

    def push(self, element):
        super().push(element)
        self.__sum += element
              

    def pop(self):
        element = super().pop()
        if element != None:
            self.__sum += element
        return element       

objsum = StackSumLifo()

objsum.push(5)
print(objsum.getSum)