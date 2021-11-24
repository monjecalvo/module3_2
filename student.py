class student():

    def __init__(self,dni,name,surnames,age,city,provinces,email):
        self.__dni = dni
        self.__name = name
        self.__surnames = surnames
        self.__age = age
        self.__city = city
        self.__provinces = provinces
        self.__email = email

    def getDNI(self):
        return self.__dni

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name    

    def getsurnames(self):
        return self.__surnames

    def setsurname(self,surname):
        self.__surname = surname      

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age
        

    def getcity(self):
        return self.__city

    def setcity(self, city):
        self.__city = city
           

    def getprovinces(self):
        return self.__provinces

    def setprovinces(self, provinces):
        self.__provinces = provinces
        return self.__provinces    

    def getemail(self):
        return self.__email

    def setemail(self, email):
        self.__email = email
        
