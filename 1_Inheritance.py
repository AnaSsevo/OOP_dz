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
    
    def get_average_hw_grade(self):
        """Вычисляет среднюю оценку за домашние задания."""
        if not self.grades:
            return 0

        total_grades = 0
        total_count = 0

        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)

        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.get_average_hw_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_hw_grade() < other.get_average_hw_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_hw_grade() == other.get_average_hw_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_hw_grade() > other.get_average_hw_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь: курс -> список оценок

    def get_average_lecture_grade(self):
        """Вычисляет среднюю оценку за лекции."""
        if not self.grades:
            return 0

        total_grades = 0
        total_count = 0

        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)

        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        avg_grade = self.get_average_lecture_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")


    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() < other.get_average_lecture_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() == other.get_average_lecture_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() > other.get_average_lecture_grade()
        return NotImplemented


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

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")



# Тестовые данные
# Создаём объекты
reviewer = Reviewer("Some", "Buddy")
lecturer = Lecturer("Some", "Buddy")
student = Student("Ruoy", "Eman", "male")

# Заполняем данные 
student.courses_in_progress = ["Python", "Git"]
student.finished_courses = ["Введение в программирование"]
student.grades = {"Python": [10, 10, 10, 9, 10, 10, 10, 10, 10, 10],
                  "Git": [10, 10, 10, 9, 10, 10, 10, 10, 10, 10]}

lecturer.courses_attached = ["Python"]
lecturer.grades = {"Python":
                   [10, 10, 10, 9, 10, 10, 10, 10, 10, 10]}

# Выводим информацию
print(reviewer)
print()
print(lecturer)
print()
print(student)


