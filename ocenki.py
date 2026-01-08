class Student:
    def __init__(self, name, gender, res):
        self.name = name
        self.gender = gender
        self.res = res
        self.grade = self.calc_grade()

    def calc_grade(self):
        return 2 + (self.res / 100) * 4

n = int(input("Num of students: "))
student = []
for i in range(n):
    data = input(f"Enter student {i+1} info (name gender points): ").split()
    name = data[0]
    gender = data[1].upper()
    points = float(data[2])
    student.append(Student(name, gender, points))

all_grades = []
f_grades = []
m_grades = []
for s in student:
    all_grades.append(s.grade)
    if s.gender == 'W': f_grades.append(s.grade)
    elif s.gender == 'M': m_grades.append(s.grade)
    else: print("Invalid gender")


if all_grades:
    avg_all = sum(all_grades) / len(all_grades)
else:
    avg_all = 0

if f_grades:
    avg_f = sum(f_grades) / len(f_grades)
else:
    avg_f = 0

if m_grades:
    avg_m = sum(m_grades) / len(m_grades)
else:
    m_all = 0

print(f"Average: {avg_all:.2f}")
print(f"M Average: {avg_m:.2f}")
print(f"W Average: {avg_f:.2f}")