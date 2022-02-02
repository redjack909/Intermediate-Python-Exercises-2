print ('imported student')

class Student:
    def __init__(self, name , gpa):
        self.name = name
        self.gpa = gpa

    def report_gpa(self):
        report = str(self.name) + " has a GPA of " + str(self.gpa)
        return  report
    
