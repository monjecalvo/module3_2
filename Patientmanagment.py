class Patientmanagment():

    def __init__(self,dni,name,surname,yearbirth,telephone,email,historyvisits,numvisits):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__yearbirth = yearbirth
        self.__telephone = telephone
        self.__email = email
        self.__historyvisits = historyvisits
        self.__numvisits = numvisits

    def getdni(self):
        return self.__dni

    def setndni(self,dni):
        self.__dni = dni

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name

    def getsurname(self):
        return self.__surname
        
    def setsurname(self,surname):
        self.__surname = surname    

    def getyearbirth(self):
        return self.__yearbirth

    def setyearbirth(self,yearbirth):
        self.__yearbirth = yearbirth    

    def gettelephone(self): 
        return self.__telephone

    def settelephone(self,telephone):
        self.__telephone = telephone    

    def getemail(self):
        return self.__email

    def setemail(self, email):
        return self.__email

    def gethistoryvisits(self):
        return self.__historyvisits

    def sethistoryvisits(self,historyvisits):
        self.__historyvisits = historyvisits

    def getnumvisits(self):
        return self.__numvisits

    def setnumvisits(self, numvisits):
        self.__numvisits = numvisits