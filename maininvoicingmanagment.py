import invoicingmanagment
import controllerinvoicing

def readid():
    while(True):
        id = int(input("Input ID"))
        if(id>0):
            return id
        else:
            print("Error ID")

def readdate():
    while(True):
        date = input("Input date")

def readNIF():
    pass

controller = controllerinvoicing.controllerinvoicing()

while(True):
    print("Add invoice")
    print("List not paid invoices: All and by Customer NIF")
    print("List paid invoices: All and by Customer NIF")
    print("Pay invoice")
    print("Exit")
    op = input("input a option")


    if(op==1):
        pass

    elif(op==2):
        pass

    elif(op==3):
        pass

    elif(op==4):
        pass

    elif(op==5):
        break