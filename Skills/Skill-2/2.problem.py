import pytest
class Doctor:
    def init(self,Name,Qualification):
        self.Name=Name
        self.Qualification=Qualification
    def doctordetails(self):
        print("Doctor Name:",self.Name,"\nQualification:",self.Qualification)

class Medicine:
    def init(self,Medicines):
        self.Medicines=Medicines
    def medicals(self):
        print("Medicinces:",self.Medicines)


class Patient(Doctor, Medicine):
    def init(self, PatientId, Patientname, Age, Disease, Doctorname,Qualification,Medicines):
        self.PatientId=PatientId
        self.PatientName=Patientname
        self.Age=Age
        self.Disease=Disease
        Doctor.init(self,Doctorname,Qualification)
        Medicine.init(self,Medicines)
    def patientdetails(self):
        print("PatientId:",self.PatientId)
        print("Patient Name:",self.PatientName)
        print("Age:",self.Age)
        print("Disease: ",self.Disease)



if name == 'main':
    c=Patient(1,"Sai",3,"Maliara","Venky","MBBS","Dichlorohexane")
    c.patientdetails()
    c.doctordetails()
    c.medicals()
    printdetails(c)

def test_testcase1():
    c = Patient(1, "Sai", 3, "Maliara", "Venky", "MBBS", "Dichlorohexane")
    assert c.Medicines== "Dichlorohexane"