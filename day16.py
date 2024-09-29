#Expectional Handling

a=int(input("enter a number"))
b=int(input("enter a number"))
print(a/b)
#enter a number6
#enter a number2
#3.0


#enter a number2
#enter a number0
#ZeroDivisionError: division by zero

#ZeroDivisionError
print("hi")
a=int(input("enter a number"))
b=int(input("enter a number"))
print(a/b)#critical statement
print("End")



print("hi")
try:
    x=int(input("enter a number:"))
    print(10/x)
except ValueError as e:
    print("please enter a number",e)
except ZeroDivisionError:
    print("division by zero is not allowed")
finally:
    print("done")

#enter a number:3
#3.3333333333333335
#done

#enter a number:a
#please enter a number invalid literal for int() with base 10: 'a'
#done

    
#enter a number:0
#division by zero is not allowed
#done



#ValueError
print("hi")
try:
    x=int(input("enter a number:"))
    if x<0:
        raise ValueError
    print(10/x)
except ValueError as e:
    print("please enter a number",e)
except ZeroDivisionError:
    print("division by zero is not allowed")
finally:
    print("done")

#hi
#enter a number:-1
#please enter a number 
#done

#hi
#enter a number:2
#5.0
#done

#hi
#enter a number:0
#division by zero is not allowed
#done

#hi
#enter a number:a
#please enter a number invalid literal for int() with base 10: 'a'
#done



    

#NameError
print("hi")
try:
    x=int(input("enter a number:"))
    if x<0:
        raise ValueError
    print(10/y)
except NameError as e:
    print("please enter a number",e)
except ZeroDivisionError:
    print("division by zero is not allowed")
finally:
    print("done")

#hi
#enter a number:2
#please enter a number name 'y' is not defined
#done

#hi
#enter a number:-1
#done

    

#PYTHON MODULES
  #Built in modules

#math
import math
help(math)


import math
print(math.pi)#3.141592653589793

import math
print(math.factorial(5))#120

import math as m
print(m.pi)#3.141592653589793

import math
print(m.factorial(5))#120

from math import factorial,pi,floor,sqrt,ceil
print(pi)#3.141592653589793
print(floor(3.9))#3
print(ceil(3.2))#4
print(sqrt(16))#4.0

#access everything
from math import *
print(pi)#3.141592653589793
print(floor(5.6))#5
print(ceil(7.3))#8
print(sqrt(100))#10.0
print(isqrt(100))#10



#datetime
import datetime 
help(datetime)

from datetime import*
x=datetime.now()

print(x)#2024-09-11 16:16:33.229140
print(x.month)#9
print(x.day)#11
print(x.hour)#16
print(x.minute)#16
print(x.second)#33
print(x.strftime('%c'))#Wed Sep 11 16:18:29 2024


from datetime import*
x=datetime.now()
y=int(input("enter your year of birth:"))
print(f"Age is {x.year-y} years")
#enter your year of birth:2002
#Age is 22 years


y=int(input("enter your year of birth:"))
print(f"{x.year-y}years {x.month-y} month {x.day} day")#22years -1993 month 11 day


from datetime import *
x=datetime.now()
y=input("Enter you year of birth :")
print(y)
z=y.split('-')
print(f"{x.year-int(z[2])} years {x.month-int(z[1])} months {x.day-int(z[0])} days ")

#Enter you year of birth :12-01-2002
#12-01-2002
#22 years 8 months -1 days 



#random
from random import *
print(random())#[0.0-1.0]

print(randint(1000,9999))#6235-changes the value everytime when it run.

  #choice-choose random
print(choice(['stone','paper','scissors']))#paper-changes the value everytime when it run.


  #shuffle
x=[1,2,3,4]
shuffle(x)
print(x)#[4, 1, 3, 2]



#string
from string import *

print(ascii_letters)#abcd in small and capital letter
print(digits)#0123456789
print(punctuation)#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(printable)#it print all these




from datetime import *
x=datetime.now()
y=input("Enter you year of birth :")
print(y)
z=y.split('-')
print(f"{x.year-int(z[2])} years {x.month-int(z[1])} months {x.day-int(z[0])} days ")


