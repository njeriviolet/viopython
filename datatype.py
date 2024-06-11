#datatype

number=78 #interger--Int
num=45.09 #float
greeting="how are you doing" #string--str
is_programming_intresting=True #boolean--bool
devices=["laptop,","computer","tablet","phone"] #list is written with special brackets
browser=("opera","firefox","safari","brave") #Tuple the list is odered and unchangable
countries={"Kenya","Uganda","Tanzania"}#set
employee={
    "firstname" : "jane",
    "age"       : 29 ,
    "nationality":"kenyan",
    "emailadress": "jane@gmail.com"
} #dictionary--dict

print(is_programming_intresting)
print(num)
print (countries)
print(employee["firstname"])  #to display a single entity in a dictionary

#determining a datatype

print(type(countries))
print(type(employee))

#typecasting is the process of converting one data type to another

print(int(num))
print(float(number))