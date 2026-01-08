class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student section: {self.section}")

student1 = Student('Anna Sivcheva', 15, 'Computer Science')
student1.display()
student1.displayStudent()