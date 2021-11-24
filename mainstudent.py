import student
import controllerstudent

def readDNI():
    list = "TRWAGMYFPDXBNJZSQVHLCKE"

    while True:

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
def readname():
    name = input("Your name ")
    
def readsurnames():
    pass

def readage():
    pass

def readcity():
    pass

def readprovinces():
    pass

def reademail():
    pass

controller = controllerstudent.controllerstudent()


while (True):

    print("Add a student" )
    print("Delete a student" )
    print("Modify a student ")
    print("Search a studnet ")
    print("Exit ")
    num = input("input a choose ")

    if (num == "1"):
        dni = readDNI()
        name = readname()
        surnames = readsurnames()
        age = readage()
        city = readcity()
        provinces = readprovinces()
        email = reademail()

        if controller.addstudnets (dni,name,surnames,age,city,provinces,email):
            print("Studnet add succefully")
        else:
            print("Error, the student is already created")    

    elif (num == "2"):
        dni = readDNI()
        Student = controller.deletestudents(dni)
        if Student != None:
            print("The student delete")
        else:
            print("The DNI no exists")

    elif (num == "3"):
        dni = readDNI()
        Student = controller.searchstudents(dni)
        if Student != None:
            print("Modification of student with DNI")
            print("Modify name ")  
            print("Modify Surname ")   
            print("Modify Age ") 
            op = input("What do you want to modify: ")
            if(op == "1"):
                NewName = readname()
                prop =  {'name': NewName}
                controller.modifysutdent(dni,prop)
            if(op == "2"):
                NewSurnames = readsurnames()
                prop =  {'Surnames': NewSurnames}
                controller.modifysutdent(dni,prop)
            if(op == "3"):
                NewAge= readage()
                prop =  {'age': NewAge}
                controller.modifysutdent(dni,prop)        
        else:
            print("The dni doesn't exists")            
    elif (num == "4"):
        dni = readDNI()
        Student = controller.searchstudents(dni)
        if Student != None:
            print("name:", Student.getname())
            print("surnames:", Student.getsurnames())
            print("email:", Student.getemail())
        else:
            print("The DNI no exists")    
    elif (num == "5"):
        break        