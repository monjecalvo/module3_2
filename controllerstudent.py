import student

class controllerstudent():

    def controllerstudent(self):
        self.__Students = {}

    def addstudnets(self,dni, name, surnames,age,city,provinces,email):
        Student = student.student(dni, name, surnames,age,city,provinces,email)
        if(dni in self.__Students.keys()):
            return False
        else:    
            self.__Students[Student.getDni()] = Student
            return True

    def deletestudents(self,dni):
        if dni in self.__Students.keys():
            Student = self.__Students.pop(dni)
            return Student
        else:
            return None

    def modifysutdent(self,dni,prop):
        Student = self.__Students[dni]
        for properties, value in prop.items():
            if (properties == "Name"):
                Student.setname(value)
            if (properties == "Surname"):
                Student.setsurname(value)
            if (properties == "Age"):
                Student.setage(value)        

    def searchstudents(self,dni):
        return self.__Students.get(dni)        