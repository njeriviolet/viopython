class Student:
    def __init__(self,firstname,course,gender):
        self.firstname=firstname
        self.course=course
        self.gender=gender
    def study(self):
        print(self.firstname,"is studying")

student1=Student("sam","cybersecurity","male")
student1.study()
student2=Student("Ann","datascience","female")
student2.study()

student3=Student("Makena","MIT","female")