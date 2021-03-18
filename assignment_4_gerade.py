
##########################################################################################
#2
##########################################################################################

def sort(d):
    d_sorted = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
    print(d_sorted)
sort(d)

###########################################################################################
# 4
###########################################################################################

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        print('running __init__\n')
        self.type_of_triangle()
        
    def __repr__(self):
        return f"I am a Triangle with sides {self.side1}, {self.side2} and {self.side3}"
        
    #def __repr__(self):
    #    return "42"
        
    def type_of_triangle(self):
        
        if self.side1 == self.side2 and self.side1 == self.side3:
            print('1')## equilaterian
            self.mytype = 'equilateral'
        elif self.side1 == self.side2 or \
             self.side1 == self.side3 or \
             self.side2 == self.side3:
            print('2') #isosceles
            self.mytype = 'isosceles'
        elif self.side1**2 + self.side2**2 != self.side3**2:
            print('0')
            self.mytype = 'no triangle'
        else:
            print('3')
            self.mytype = 'scalene'
tri= Triangle(5,5,5)

###############################################################################################
#6
###############################################################################################
class employee:
    def __init__(self, name, ssid, salary, department):
        self.name= name
        self.ssid= ssid
        self.salary = salary
        self.department = department
        self.bonus()
    def bonus(self):
        self.newsalary = salary*1,1

class manager(employee):
    def __init__(self, name, ssid, salary, department, password, numberOfEmployees):
        self.name= name
        self.ssid= ssid
        self.salary = salary
        self.department = department
        self.bonus()
        self.password = password
        self.numberOfEmployees = numberOfEmployees
        self.authenticate_password
    def bonus():
        self.newsalary = salary*1,15
    def authenticate_password(x):
        valid = x == password
        print(valid)
