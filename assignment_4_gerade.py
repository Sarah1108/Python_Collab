
##########################################################################################
#2
##########################################################################################

#def sort(d):
#    d_sorted = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
#    print(d_sorted)
#sort(d)

###########################################################################################
# 4
###########################################################################################

#class Triangle:
#    def __init__(self, side1, side2, side3):
#        self.side1 = side1
#        self.side2 = side2
#        self.side3 = side3
#        print('running __init__\n')
#        self.type_of_triangle()
        
#    def __repr__(self):
#        return f"I am a Triangle with sides {self.side1}, {self.side2} and {self.side3}"
        
    #def __repr__(self):
    #    return "42"
        
#    def type_of_triangle(self):
#        
#        if self.side1 == self.side2 and self.side1 == self.side3:
#            print('1')## equilaterian
#            self.mytype = 'equilateral'
#        elif self.side1 == self.side2 or \
#             self.side1 == self.side3 or \
#             self.side2 == self.side3:
#            print('2') #isosceles
##            self.mytype = 'isosceles'
#        elif self.side1**2 + self.side2**2 != self.side3**2:
#            print('0')
#            self.mytype = 'no triangle'
#        else:
#            print('3')
#            self.mytype = 'scalene'
#tri= Triangle(5,5,5)

###############################################################################################
#6
###############################################################################################
##AKTUEL:
class employee:
    def __init__(self, name, ssid, salary, department): #password= None, numberOfEmployees= 0):
        self.name = name
        self.ssid = ssid
        self.salary = salary
        self.department = department
        self.bonus()
    def bonus(self):
        self.newsalary = self.salary*1,1
        return self.newsalary
    #def name(self):
        #return self.name

class manager(employee):
    def __init__(self, name, ssid, salary, department, password, numberOfEmployees):
        employee.__init__(self, name, ssid, salary, department)#, password, numberOfEmployees)
        self.name= name
        self.ssid= ssid
        self.salary = salary
        self.department = department
        self.bonus()
        self.password = password
        self.numberOfEmployees = numberOfEmployees
        self.authenticate_password
    def bonus(self):
        self.newsalary = self.salary*1,15
        return self.newsalary
    def authenticate_password(password1, self):
        if password1 == self.password is False:
            password_authentification = False
        else: 
            passworkd_authentificatio = True 

f1 = employee("John",12345678900,2500,"TI")
f2 = employee("Paul",12345678901,1800,"TI")
f3 = manager("Marta",23456789012,6000,"TI",101101,2)##instead of employee
# It didn't work with f1.name(), or any argument(), so we removed them
#f1.name
#f2.ssid
#f3.department
############## only worked when class f3 changed to manger instead of employee as that class does not have authenticate_password
#f3.bonus()
f3.authenticate_password(101101)

####ALTE VERSION#################################################################
#################################################################################################################
#class employee:
 #   def __init__(self, name, ssid, salary, department, password= None, numberOfEmployees= 0):
  #      self.name = name
   #     self.ssid = ssid
    #    self.salary = salary
     #   self.department = department
       # self.bonus()
    #d#ef bonus(self):
    #    self.newsalary = self.salary*1,1
    #def name(self):
    #    #return self.name

#class manager(employee):
#    def __init__(self, name, ssid, salary, department, password, numberOfEmployees):
#        self.name= name
#        self.ssid= ssid
#        self.salary = salary
#        self.department = department
#        self.bonus()
#        self.password = password
#        self.numberOfEmployees = numberOfEmployees
#        self.authenticate_password
#    def bonus(self):
#        self.newsalary = self.salary*1,15
#    def authenticate_password(password1, self):
#       password1 == self.password

#f1 = employee("John",12345678900,2500,"TI")
#f2 = employee("Paul",12345678901,1800,"TI")
#f3 = employee("Marta",23456789012,6000,"TI",101101,2)

#f2.bonus() 
