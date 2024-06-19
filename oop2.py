class Car:
    def __init__(self, model,color,manufacturer, yop):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop


    def speed(self):
        print("The manufacturer of",self.model,"is",self.manufacturer)

car1=Car("B12","white","BMW",2014)
car1.speed()
car1=Car("M12","blue","MAZDA",2022)
car1.speed()
car1=Car("B16","white","BMW",2014)
car1.speed()
car1=Car("B12","pear","BMW",2034)
car1.speed()
car1=Car("B15","orange","BMW",2014)
car1.speed()
car1=Car("B12","white","BMW",2014)
car1.speed()