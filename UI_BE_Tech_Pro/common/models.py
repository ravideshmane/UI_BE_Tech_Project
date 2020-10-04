from django.db import models


# Create your models here.
class Designation(models.Model):
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.designation


class TechStack(models.Model):
    tech_stack = models.CharField(max_length=50)

    def __str__(self):
        return str(self.tech_stack)


class EmploymentType(models.Model):
    employment_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.employment_type)


class User(models.Model):
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user