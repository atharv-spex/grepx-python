#list.py
#indexing
numbers = [10,20,30,40,50]
print(numbers[0])#first
print(numbers[-1])#last
print("--" * 20)
#Slicing
numbers = [10,20,30,40,50,60]
print(numbers[1:4])
print(numbers[:3])
print("--" * 20)
#append/insert/remove/pop
numbers = [10,20,30]
numbers.append(40)
print(numbers)
numbers.insert(1,15)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.pop()
print(numbers)
print
#sort/sorted
numbers = [50,10,20,40,30]
numbers.sort()
print("sorted numbers;",numbers)
#reverse
number = [1,2,3,4,5]
number.reverse()
print("reversed numbers:",number)
#min/max/sum
numbers = [10,30,50,70]
print("min:",min(numbers))
print("max:",max(numbers))
print("sum:",sum(numbers))
print("--" * 20)
#list copy
a = [1,2,3]
b = a.copy()
b.append(4)
print("a:",a)
print("b:",b)
print("--" * 20)
#nested list
matrix = [[1,2],[3,4]]
print(matrix[0])
print(matrix[1])
print(matrix[0][1])
print("--" * 20)
#list membership(in/ in not)
numbers = [10,20,30]
print(20 in numbers)
print(40 in numbers)