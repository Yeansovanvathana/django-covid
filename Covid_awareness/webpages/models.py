from django.db import models

# Create your models here.
class ProfileImage(models.Model):
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
class QuestionSurvey(models.Model):
    q1 = models.BooleanField()
    q2 = models.BooleanField()
    q3 = models.BooleanField()
    q4 = models.BooleanField()

