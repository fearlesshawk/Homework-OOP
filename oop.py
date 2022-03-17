#    def average(grade): 
#            ave = float(sum(grade)) / len(grade)
#            return print(ave)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = {}
        
        
    def rate_works(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
#    def average(grade): 
#            ave = float(sum(grade)) / len(grade)
#            return print(ave)
        
    def __str__(self):
            profile = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average(g)} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses} '
            return profile
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = {}
        self.grades = {}
        
#    def average(grade): 
#            ave = float(sum(grade)) / len(grade)
#           return ave
        
    def __str__(self):
            profile = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.ave}'
            return profile

tom = Student("Tom", "Soyer", 'boy')
#print(tom.surname)     #Soyer

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = {}
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
            profile = f'Имя: {self.name}\nФамилия: {self.surname}'
            return profile

    
#print(tom)

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
 
#print(best_student.grades)