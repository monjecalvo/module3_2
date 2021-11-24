import Patientmanagment

class controllerpatientmanagment():
    
    def controllerpatients(self):
        self.__patients = {}

    def addpatientss(self,dni,name,surname,yearbirth,telephone,email,historyvisits,numvisits):
        patient = Patientmanagment.Patientmanagment(dni,name,surname,yearbirth,telephone,email,historyvisits,numvisits)
        if(dni in self.__patients.keys()):
            return False
        else:    
            self.__patients[patient.getDni()] = patient
            return True

    def deletepatients(self,dni):
        if dni in self.__patients.keys():
            patient = self.__patients.pop(dni)
            return patient
        else:
            return None

    def searchpatients(self,dni):
        return self.__patients.get(dni)

    def searchhistory(self,historyvisits):
        return self.__patients.get(historyvisits)    