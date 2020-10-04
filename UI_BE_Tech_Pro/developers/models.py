from django.db import models

# Create your models here.
from common.models import Designation, TechStack, EmploymentType

from common.models import User


class Developers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE, null=True, blank=True)
    tech_stack = models.ManyToManyField(TechStack, null=True, blank=True)
    total_experience = models.FloatField()
    employment_type = models.ForeignKey(EmploymentType,on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=64)
    annual_ctc = models.FloatField()
    linked_in_profile = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.user)

