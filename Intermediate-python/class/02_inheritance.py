# Parent Clss
class Person:
    status = "Alive"
    
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
    def introduce(self):
        return f"Hello my name is {self.name} and I'm  {self.age} years old"
    


class Employee(Person):
    
    def __init__(self,name,age, job) -> None:
        self.job = job
        super().__init__(name,age)
        
    def emp_info(self):
        return f"My name is {self.name} and age is {self.age} and works as a {self.job}"
        
        


emp_one = Employee(name="sam",age=22,job="Ai Enginerr")
print(emp_one.emp_info())
print(emp_one.status)