# class is a blueprint for creating objects
# objects are instance of a class, that can hold data and have some behavior

class Person:
    # class attribute
    age:str = "Ai Engineer"
    # private class atribute
    __seeks:str = "A passionate flavour"
    
    # constructor
    def __init__(self, name,age):
        # instance attribute
        self.name = name
        self.__age= age
        
    def greet(self):
        return f"Hello {self.name} ! Good morning"
    
    def get_private_data(self):
        return self.__age
    
    def get_seek(self):
        return self.__seeks



person_one = Person("Sam", 22)
print(person_one.greet())

person_two = Person(name="Rammy", age=33)
print(person_two.greet())


print(person_two.get_private_data())

print(person_one.get_seek())