from django.db import models
from auth_system.models import CustomUser
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biography")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")

    def __str__(self):
        return f"Профіль користувача {self.user.username}"

    #def get_absolute_url(self):
    #    return reverse('profile_detail', kwargs={'username': self.user.username})