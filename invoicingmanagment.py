class invoicingmanagment():

    def __init__(self,id,date,NIF,paid,base,VAT,total,invoicelines):
        self.__id = id
        self.__date = date
        self.__NIF = NIF
        self.__paid = paid
        self.__base = base
        self.__VAT = VAT
        self.__total = total
        self.__invoicelinies = invoicelines

    def getid(self):
        return self.__id

    def setname(self,id):
        self.__id = id

    def getdate(self):
        return self.__date

    def setdate(self,date):
        self.__date = date

    def getNIF(self):
        return self.__NIF

    def getpaid(self):
        return self.__paid

    def setpaid(self,paid):
        self.__paid = paid    

    def getbase(self): 
        return self.__base

    def setbase(self,base):
        self.__base = base    

    def getVAT(self):
        return self.__VAT

    def setVAT(self, VAT):
        return self.__VAT

    def gettotal(self):
        return self.__total

    def settotal(self,total):
        self.__total = total

    def getinvoicelines(self):
        return self.__invoicelinies

    def setinvoicelinies(self, invoicelinies):
        self.__invoicelinies = invoicelinies