# print("randomization")
class Human:
    gender = "Female"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

class Employee(Human):
    pass

mustafa = Employee("Mustafa","38")
print(mustafa)
