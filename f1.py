class Person:
    def __init__(self, first, last, role):
        self.first = first
        self.last = last
        self.role = role

    @property
    def fullname(self):
        full_name = self.first + ' ' + self.last
        return full_name

    def details(self):
        full_name = self.first + ' ' + self.last
        role = self.role
        return (full_name + ' ' + '==>' + ' ' + role)

    @classmethod
    def Example(cls, String):
        first, last, role = String.split('-')
        return cls(first, last, role)


if __name__ == '__main__':
    x = Person('Jawad', 'Hussain', 'developer')
    print(x.first)
    print(x.last)
    print(x.role)
    print(x.fullname)
    y = x.details()
    print(y)
    print('========================================================================================')
    p1 = Person.Example('Jawad-Hussain-Developer')
    print(p1.first)
    print(p1.last)
    print(p1.fullname)
    print(p1.role)
    print(p1.details())
    print('========================================================================================')
    p3 = Person.Example('test1-user1-admin')
    print(p3.first)
    print(p3.last)
    print(p3.fullname)
    print(p3.role)
    print(p3.details())
    print('========================================================================================')