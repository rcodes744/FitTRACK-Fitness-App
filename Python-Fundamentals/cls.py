class Person:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g
    def _str_(self):
        return f'Name:{self.name},age:{self.age}'

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}')

    def is_adult(self):
        return self.age >= 18

p1 = Person("Alice", 17, "Female")
p1.display_info()
print("Is adult:", p1.is_adult())

class Student(Person):
    def __init__(self, n, a, g, c, p, college):  # Added 'college' parameter [web:1]
        super().__init__(n, a, g)


"""
# Inheritance

class Student(Person):
    def __init__(self, n, a, g, c, p, college):  # Added 'college' parameter [web:1]
        super().__init__(n, a, g)
        self.course = c
        self.program = p
        self.college = college  # Now matches parameter
    
    def college_info(self):
        print(f'College: {self.college}, Program: {self.program}')

s1 = Student("Bob", 20, "Male", "CS101", "B.Tech", "MIT")
s1.display_info()  # Finds Person.display_info() → "Name: Bob, Age: 20, Gender: Male"
print("Is adult:", s1.is_adult())  # Finds Person.is_adult() → True (20 ≥ 18)
s1.college_info()  # Finds Student.college_info() → "College: MIT, Program: B.Tech"
"""

#project lab 
#lab 15 mini project=personal fitness tracker.jpynb
# create table data base

