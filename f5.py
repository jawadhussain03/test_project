import f1

x = f1.Person('Jawad', 'Hussain', 'Developer')
print("========================Using instance method=============================")
print(x.fullname)
print(x.details())
print("========================Using class method================================")
y = f1.Person.Example('Jawad-Hussain-Developer')
print(y.fullname)
print(y.details())

