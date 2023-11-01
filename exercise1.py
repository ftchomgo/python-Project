print('Hello world')
#this is python comment in one line
print('comment in one line')
"""this is a python
comment written in 
multiple lines"""
print("multiline comment")
name = 'estephe'
age =26
weight=67.6
print(name)
print(age)
print(weight)
firstname='Fabien'
my_age=284
session="March2023"
print("my first name is",firstname, "i am ",my_age , "years old and ", "taking DevOps for", session)
current_year=2023
birth_year=1739
print(current_year-birth_year)
best_fruit="Orange"
print(best_fruit)
print(type(3))
print(type(10.5))
print(type(age))
import statistics
print("the standard deviation of the list [1,2.,3,5,6.7,3.2,4.9] is",statistics.stdev([1,2.,3,5,6.7,3.2,4.9]))
c=5+4j
print(type(c))
greeting="hello everyone!!"
print(greeting[2:8])
print(greeting[:10])
print(greeting[5:])
print(greeting[-16:-11])
Fullname=firstname + " " + name
print(Fullname)
x="Hello World"
print(x.upper())
print(x.lower())
print(x.replace("World", "students of March2023 session"))
b1=7>7.1
b2=7==7
b3=7<7.1
print("7>7.1 is",b1,"7==7 is", b2,"7<7.1 is", b3)
drinks=("beer", "water", "coke", "wine", "juice")
my_tuple1=(16, 2.5, "why", False)
my_tuple2=16,2.5, "hello", True
print(my_tuple1,my_tuple2, drinks)
drink2=["beer", "water", "coke", "wine", "juice"]
print(drink2)
drink3=["beer", "water", "coke", "wine", "juice", "mimbo"]
print(drink3[-5:-2])
s="welcome"
s1=s[0:3:1]
s2=s[3:0:-1]
print(s1,s2)
import sys
sys.maxsize
import os
os.getcwd()
import math
import statistics
print(math.pi)
print(math.e)
print(statistics.stdev([0, 2, 7, 20, 18, 13, 10]), statistics.mean([0, 2, 7, 20, 18, 13, 10]))
#import matplotlib.pyplot as plt
#x=[24,25,26, 10, 8]
#y=[23,24,25, 9, 4]
# plt.plot(x,y)
# plt.show()
import Students
print(Students.getITNames)
print(Students.getNoneITNames)