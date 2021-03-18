####################################################################################################
#2
#####################################################################################################
#import math

#def distance(ax,ay,bx,by):
#    step1= ((ax-bx)**2) + (ay-by)**2
#    dis = math.sqrt(step1)
#    print(dis)
#distance(1,3,4,2)
#######################################################################################################
#4
########################################################################################################

#roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

#def Roman_to_int(t):
    
#    resultI = 0
#    for k,v in roman_numerals.items():          
#        if t == k:
#            resultI += roman_numerals.get(t)
#        else:
#            for i in t:
#                if i in roman_numerals.keys():
#                    if i == k:
 ##                       resultI += v
#    print(resultI)
#Roman_to_int("M")

#roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}

#####not finished yet
#def int_to_Roman(t):
#    result2 = 0 
#    for k,v in roman_numerals.items():
#        if t == v:
#            result2 = roman_numerals.get(t)
#    print(result2)
#int_to_Roman(50)

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