class My :
    def __init__ (self,name,age,work):
        self.name = name
        self.age = age
        self.work = work

name = str(input('Enter Your Name : '))
age = int(input('Enter Your Age : '))
work = input('Enter Your Work : ')
p1 = My(name, age, work)
print("My Name is ",p1.name)
print("I am ",p1.age,'is old')
print('I Work is',p1.work)