class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def studentdata(self):
        print("Name: {} marks: {}")


s1 = Student("violet",50)
s1.studentdata()
s2=  Student("Ann",45)
s2.studentdata()

print("Name: {} marks: {}".format(s1.name, s1.marks))
print("Name: {} marks: {}".format(s2.name, s2.marks))

























