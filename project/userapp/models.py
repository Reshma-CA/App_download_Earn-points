from django.db import models

# Create your models here.


# Create your models here.
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class People(models.Model):
    username = models.CharField(max_length=200,unique=True)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password =models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=255)
    app_link = models.URLField()
    points = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='apps')
    app_image = models.ImageField(upload_to='app_images/', blank=True, null=True)

    def __str__(self):
        return self.name    

class UserProfile(models.Model):
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    user_points = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)  # Track the number of completed tasks

  

    def __str__(self):
        return f"{self.user.username} - Points: {self.user_points}, Tasks Completed: {self.tasks_completed}"

class Task(models.Model):
    name = models.CharField(max_length=255)
    app = models.ForeignKey('App', on_delete=models.CASCADE, related_name='tasks')
    screenshot = models.ImageField(upload_to='task_screenshots/', storage=fs)
    points_awarded = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    user_profile = models.ForeignKey('UserProfile', related_name='tasks', on_delete=models.CASCADE)
    # ocr_text = models.TextField(blank=True, null=True)  # To store the extracted text

    def __str__(self):
        return f"Task: {self.name} for {self.user_profile.user.username}"

    