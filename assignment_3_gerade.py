####################################################################################################
#2
#####################################################################################################
import math

def distance(ax,ay,bx,by):
    step1= ((ax-bx)**2) + (ay-by)**2
    dis = math.sqrt(step1)
    print(dis)
distance(1,3,4,2)
#######################################################################################################
#4
########################################################################################################

roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

def Roman_to_int(t):
    
    resultI = 0
    for k,v in roman_numerals.items():          
        if t == k:
            resultI += roman_numerals.get(t)
        else:
            for i in t:
                if i in roman_numerals.keys():
                    if i == k:
                       resultI += v
    print(resultI)
Roman_to_int("M")

int_roman = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",5:"V",4:"IV",1:"I"}

#####not finished yet
def int_to_Roman(t):
    result2 = "" 
    for k,v in int_roman.items():
        if t == v:
            result2 += int_roman.get(v)
        elif result2 == "":
            for i in int_roman.keys():
                if i == k:
                    result2 += v
    print(result2)
int_to_Roman(1500)

#########################tried this from : https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
#########################didn't work either
#def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

#    if not isinstance(input, type(1)):
#        raise TypeError ("expected integer, got %s" % type(input))
#    if not 0 < input < 4000:
#        raise ValueError ("Argument must be between 1 and 3999")
#    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
#    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
#    result = []
#    for i in range(len(ints)):
#        count = int(input / ints[i])
#        result.append(nums[i] * count)
#        input -= ints[i] * count
#    return ''.join(result) 
#    print(result)
#int_to_roman(50)

##################################################################################################
#6
##################################################################################################
def matches(list,n): 
    r = []

    for i in list:
        temp = []
        for i in list: 
            if i not in temp:
                if len(temp) < n: 
                    temp.append(i)
                #return temp
        r.append(tuple(temp))
    print(r)
    
matches([1,2,3,4],2)