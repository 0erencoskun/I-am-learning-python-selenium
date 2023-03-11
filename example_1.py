#variable types
#Numbers,Strings,List,Tuple
#1-Numbers
print("-------------------------")
print("Numbers")
variable1 = 100 #integers are used, decimal not used(int)
variable2 = 10.1 #decimal are used(float)
variable3 = 8.5j #complex numbers are used (complex)
print(variable1)
print(variable2)
print(variable3)
#2-Strings
print("-------------------------")
print("Strings")
variable4 = 'Eren' #strings are used
variable5 = '* / + -' #different characters can be printed
print(variable4)
print(variable5) 
print(variable4*5) #asterisk multiple printable 

print("-------------------------")
#3-List
print("List")
variable6 = ['Eren','İstanbul','2004']
print(variable6)
print(variable6[1])

#Tuples
print("-------------------------")
print("Tuples")
variable7 = ('Eren','İstanbul','2004')
print(variable7)
print(variable7[0])
#Booleans
print("-------------------------")
print("Booleans")
variable8 = 1==1
print(variable8)

############################################

work1 = 4
work2 = 5

if work1>work2:
    print("work1 larger than work2")
else:
    print("work2 larger than work1")
