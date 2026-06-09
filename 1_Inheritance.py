class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        # Проверка: объект должен быть экземпляром Lecturer
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: объект не является лектором!")
            return None
        
        # Проверка: студент должен быть записан на курс
        if course not in self.courses_in_progress:
            print(f"Ошибка: вы не записаны на курс '{course}'!")
            return None

        # Проверка: лектор должен быть прикреплён к курсу
        if course not in lecturer.courses_attached:
            print(f"Ошибка: лектор не прикреплён к курсу '{course}'!")
            return None
        
        # Проверка: оценка должна быть в диапазоне 1–10
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10 баллов!")
            return None

        # Добавляем оценку в словарь лектора
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]

        return None


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь: курс -> список оценок

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    
    def rate_hw(self, student, course, grade):
        # Проверка: объект должен быть экземпляром Student
        if not isinstance(student, Student):
            print("Ошибка: можно ставить оценки только студентам!")
            return None

        # Проверка: курс должен быть в progress или finished у студента
        if course not in student.courses_in_progress and course not in student.finished_courses:
            print(f"Ошибка: студент не учится на курсе '{course}'!")
            return None

        # Проверка: ревьюер должен быть прикреплён к курсу
        if course not in self.courses_attached:
            print(f"Ошибка: ревьюер не прикреплён к курсу '{course}'!")
            return None

        # Проверка: оценка должна быть в диапазоне 1–10
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10 баллов!")
            return None

        # Добавляем оценку в словарь студента
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]

        return None

# Тестовые данные
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Тесты
print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))   # Ошибка: лектор не прикреплён к курсу 'Java'!
print(student.rate_lecture(lecturer, 'C++', 8))    # Ошибка: вы не записаны на курс 'C++'!
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка: можно оценивать только лекторов!

print(lecturer.grades)  # {'Python': [7]}

