#string3.py
text = " i love python programming "
print ("Postion of python",text.find("python"))
new_text = text.replace("python","java")
print("after replace", new_text)
#split and join
sentence = " apple banana mango"
words = sentence.split()
print("split",words)

email = "student@gmail.com"
print("started with students:",email.startswith("student"))
print("ends with:",email.endswith(".com"))