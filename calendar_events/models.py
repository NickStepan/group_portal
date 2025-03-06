from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    completed = models.BooleanField(default=False)  # Додаємо поле виконання

    def __str__(self):
        return f"{self.title} - {self.date}"
