# class is a blueprint for creating objects
# objects are instance of a class, that can hold data and have some behavior

class Person:
    # class attribute
    age:str = "Ai Engineer"
    
    # constructor
    def __init__(self, name,age):
        # instance attribute
        self.name = name
        self.age= age
        
    def greet(self):
        return f"Hello {self.name} ! Good morning"
    



person_one = Person("Sam", 22)
print(person_one.greet())

person_two = Person(name="Rammy", age=33)
print(person_two.greet())


print(person_two.age)