class Student:
    def __init__(self, name, student_id, year):
        self.name = name
        self.student_id = student_id
        self.year = year

    def introduce(self):
        return f"Hi, I am {self.name}, Year {self.year}"

    def get_id(self):
        return self.student_id


# Creating objects (instances)
stu1 = Student("Amara", "S001", 11)
stu2 = Student("Kai", "S002", 12)

print(stu1.introduce())
# Output: Hi, I am Amara, Year 11