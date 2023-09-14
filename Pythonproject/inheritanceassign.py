# 1.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    def engine_on (self):
        print("Car engine started.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, milage):
        super().__init__(make, model)
        self.milage = milage

    def speed (self):
        print("Motorcycle accelerating.")


# Creating instances of  classes
car1 = Car("BMW", "BMW X5", "Blue")
motorcycle1 = Motorcycle("Honda", "Grom", 120)


print(car1.make)
print(motorcycle1.model)

car1.engine_on()
motorcycle1.speed()
# 2.
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

    def display_details(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Bonus: {self.bonus}"


class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language

    def display_details(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Language: {self.programming_language}"



manager = Manager(1, "Pratik", 89000, 4000)
developer = Developer(2, "Aditya", 78999, "Python")

print(manager.display_details())
print(f"Manager's Total Salary: ${manager.calculate_salary()}")

print(developer.display_details())
print(f"Developer's Total Salary: ${developer.calculate_salary()}")
