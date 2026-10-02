from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    profile_image = models.ImageField(
        upload_to="students/profile_images/",
        blank=True,
        null=True,
    )

    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name
