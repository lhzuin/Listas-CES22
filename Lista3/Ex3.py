class Subjects():
    def __init__(self, type, name, grade):
        self.type = type
        self.name = name
        self.grade = grade

class STEM(Subjects):
    def __init__(self, name, grade):
        type = "STEM"
        super().__init__(type, name, grade)

class Person():
    def __init__(self, age, gender, name):
        self.age = age
        self.gender = gender
        self.name = name

class Child(Person):
    def __init__(self, age, gender, name, parents):
        super().__init__(age, gender, name)
        self. parents = parents
        print(f'{self.name} is a child')
    def miss_parents(self):
        print(f'{self.name} is missing his parents')

class Student(Person):
    def __init__(self, age, gender, name):
        super().__init__(age, gender, name)
        print(f'{self.name} is a student')

    def study(self):
        print(f'{self.name} started studying')

class Teen(Person):
    def hang_out_with_friends(self):
        print(f'{self.name} went out with his friends')

class KinderGardenKid(Child, Student):
    def __init__(self, age, gender, name, parents):
        super().__init__(age, gender, name, parents)
        print(f'{self.name} is a child who studies in Kinder Garden')
    def basics(self):
        super().miss_parents()
        super().study()

class HighSchoolTeen(Teen, Student):
    def __init__(self, age, gender, name, subjects):
        self.subjects = subjects
        super().__init__(age, gender, name)
        print(f'{self.name} is a teenager who studies in High School')
    def basics(self):
        super().hang_out_with_friends()
        super().study()
    def list_subjects(self):
        print(f'{self.name} studies '+ self.subjects.name)

subject = STEM("Math", 8)
stud1 = KinderGardenKid(3, "male", "Jorge", "Julia and John")
stud2 = HighSchoolTeen(16, "male", "Peter", subject)
stud1.basics()
stud2.basics()
stud2.list_subjects()