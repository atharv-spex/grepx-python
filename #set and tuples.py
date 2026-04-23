#set and tuples
#1.tuple creation  #once assigned value cannot be changed in tuple
data = ("rahul",25,"Nagpur")
print(data)
print(data[0])
#2.tuple indexing
person = ("Amit",30,"Pune")
name,age,city = person
print(name),(age),(city)
print(age)
print(city)
#3.name tuple
from collections import namedtuple
student = namedtuple ("student",["name","age"])
S1 = student ("Rahul",20)#first declare the value then assign the value
print(S1.name)
print(S1.age)
#set creation  # {} = set , [] = list , () = tuple
numbers = {1,2,3,4,5,6,7,}
print(numbers)#duplicate numbers #duplicate numbers cannot be used
#set operation
a = {1,2,3}
b = {3,4,5,}
print("union",a|b)
print("intersection",a&b)
print("difference",a-b)
#frozen set
fs = frozenset ([1,2,3,])
print(fs)
#set membership
numbers = {10,20,30}
print(20 in numbers)

