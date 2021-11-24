import Patientmanagment
import controllerpatientmanagment

def readName():
    name = input("Input name")
    

def readDni():
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    nif = input("DNI: ")
    if (len(nif) == 9):
        letraControl = nif[8].upper()
        dni = nif[:8]
        if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
            if tabla[int(dni)%23] == letraControl:
                return dni
    else:
        print("Error Validation")

def readSurame():
    pass

def readEmail():
    pass

def readTelephone():
    while True:
        tlf = int(input("Enter telephpone number: "))
        if (len(tlf) == 9):
            if(tlf<100000000 or tlf>999999999):
                return tlf
            else:
                print("Error")    
                
            
        

def readBirth():
    pass

controller = controllerpatientmanagment.controllerpatientmanagment()

while True:
    print("1.-Add Patient ")
    print("2.-Delete Patient ")
    print("3.-Get Patient History ")
    print("4.-List patients ")
    print("5.-Add appointment ")
    print("6.-Exit ")
    op = input("Chosse option: ")
    
    if op == 1:
        pass

    elif op == 2:
        pass

    elif op == 3:
        pass

    elif op == 4:
        pass

    elif op == 5:
        pass

    elif op == 6:
        break