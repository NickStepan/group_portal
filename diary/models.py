from django.db import models

# Create your models here.



class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Subject(models.Model):
    title = models.CharField(max_length=150) # Назва предмету
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="subjects") #Вчитель, який веде предмет
    
    #comment_teacher = models.CharField(max_length=150) #Примітка лише для вчителя
    

    def __str__(self):
            return f"{self.title}, {self.teacher}"

# Модель студента
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    student_class = models.CharField(max_length=50)
    #subjects = models.ManyToManyField(Subject, related_name="students", blank=True, verbose_name="Предмети")
    #created_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.student_class} class"



class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")
    day = models.DateField()
    is_final = models.BooleanField(default=True) #Остаточна(True) оцінка чи олівцем(False)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.student} {self.subject} {self.mark}"



class Day(models.Model):
    day = models.IntegerField() #День місяця 1до31
    month = models.IntegerField()
    "Створити день і прив'язати до нього предмети"


class Diary(models.Model):
    day = models.DateField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name="students")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name="subjects", null=True)
        
    observation = models.CharField(max_length=250) #Примітка, поле для зауваження примітки

class Schedule(models.Model):
    pass
