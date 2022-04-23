class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = {}
        self.avg = {}

    def av_mark_st(self):
        for course_name, grade in self.grades.items():
            self.average_grade[course_name] = sum(grade)/len(grade)

    def rate_lec(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress and isinstance(lecturer, Lecturers):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('ошибка добавления оценки лектора студентом')

    def __str__(self):
        return f'Студенты \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка по курсам: {self.average_grade}  \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        for course_name, grade in self.average_grade.items():
            for course_name_2, grade_2 in other.average_grade.items():
                if course_name == course_name_2:
                    if grade > grade_2:
                        self.avg[course_name] = True
                    else:
                        self.avg[course_name] = False
        return print ('Средняя оценка больше:', self.avg)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and isinstance(cool_mentor, Reviewer):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('ошибка добавления оценки студента преподавателем')

class Lecturers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average_grade = {}
        self.avg = {}

    def av_mark_lec(self):
        for course_name, grade in self.grades.items():
            self.average_grade[course_name] = sum(grade) / len(grade)

    def __str__(self):
        return f'Лекторы \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка по курсам: {self.average_grade}  \nЧитаемые лекции: {", ".join(self.courses_attached)} '

    def __gt__(self, other):
        if not isinstance(other, Lecturers):
            print('Не лектор.')
            return
        for course_name, grade in self.average_grade.items():
            for course_name_2, grade_2 in other.average_grade.items():
                if course_name == course_name_2:
                    if grade > grade_2:
                        self.avg[course_name] = True
                    else:
                        self.avg[course_name] = False
        return print ('Средняя оценка больше:', self.avg)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Ревьюеры \nИмя: {self.name} \nФамилия: {self.surname}'


best_student = Student('San', 'Choi', 'man')
best_student.courses_in_progress += ['Python', 'Git']

best_student2 = Student('Jennie', 'Kim', 'women')
best_student2.courses_in_progress += ['Python', 'Git']

cool_mentor = Reviewer('Jay', 'Park')
cool_mentor.courses_attached += ['Python', 'Git']
cool_lector = Lecturers('Hong', 'Kim')
cool_lector.courses_attached += ['Python', 'Git']
cool_lector2 = Lecturers('Yunho', 'Jeung')
cool_lector2.courses_attached += ['Python', 'Git']

# # Оценки студентам
# cool_mentor.rate_st(best_student, 'Python', 3)
# cool_mentor.rate_st(best_student, 'Git', 4)
# cool_mentor.rate_st(best_student, 'Python', 6)
# cool_mentor.rate_st(best_student, 'Git', 10)
# cool_mentor.rate_st(best_student2, 'Python', 5)
# cool_mentor.rate_st(best_student2, 'Git', 1)
# cool_mentor.rate_st(best_student2, 'Python', 3)
# cool_mentor.rate_st(best_student2, 'Git', 4)

# Оценки лекторам
# best_student.rate_lec(cool_lector, 'Git', 6)
# best_student.rate_lec(cool_lector, 'Git', 6)
# best_student.rate_lec(cool_lector, 'Python', 3)
# best_student.rate_lec(cool_lector, 'Python', 6)
# best_student.rate_lec(cool_lector2, 'Git', 8)
# best_student.rate_lec(cool_lector2, 'Git', 2)
# best_student.rate_lec(cool_lector2, 'Python', 10)
# best_student.rate_lec(cool_lector2, 'Python', 9)
#
# print(cool_lector.grades)
# print(best_student.grades)

# cool_lector.av_mark_lec()
# cool_lector2.av_mark_lec()
# print(cool_lector.__str__())
# print(cool_lector2.__str__())
# cool_lector2 > cool_lector

#best_student.av_mark_st()
#print (best_student.__str__())
#best_student2.av_mark_st()
#print (best_student2.__str__())

#best_student > best_student2

# cool_mentor.av_mark_lec()
#print (cool_mentor.__str__())
