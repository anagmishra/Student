class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person): #Parent class/Base class
    def __init__(self, name, age, school_class, house, class_teacher):
        super().__init__(name)
        self.age = age
        self.school_class = school_class
        self.house = house
        self.class_teacher = class_teacher

    def show_details(self): #Child class/Derived class
        print("The details of the student are:")
        print(f"The age of the student is: {self.age}")
        print(f"The class of the student in the school is: {self.school_class}")
        print(f"The house of the student is: {self.house}")
        print(f"The class teacher of the student is: {self.class_teacher}")

Student1=Student("Anag", 15, "10 G", "Aquila", "Srijita")
Student1.greet()
Student1.show_details()


