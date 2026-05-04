from django.db import models
from django.contrib.auth.models import User

class EyeDisease(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='diseases/', blank=True, null=True)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    prevention_tips = models.TextField()
    daily_care_tips = models.TextField()
    home_care = models.TextField()
    important_note = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class SelfAssessmentQuestion(models.Model):
    disease = models.ForeignKey(EyeDisease, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=500)
    
    def __str__(self):
        return self.question

class UserAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    possible_conditions = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.date_taken}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_date = models.DateField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"