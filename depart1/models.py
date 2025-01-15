from django.contrib.auth.models import User
from django.db import models

class Resident(models.Model):
    RES_LNAME = models.CharField(max_length=50)
    RES_FNAME = models.CharField(max_length=50)
    RES_MNAME = models.CharField(max_length=50, null=True, blank=True)
    RES_NICKNAME = models.CharField(max_length=50, null=True, blank=True)
    RES_DOB = models.DateField()
    RES_AGE = models.IntegerField(null=True, blank=True)  # Optional, can calculate dynamically
    RES_SEX = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    RES_GENDER = models.CharField(max_length=10, null=True, blank=True)
    RELIG_ID = models.IntegerField()
    RES_CIVIL_STATUS = models.CharField(
        max_length=20,
        choices=[('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced'), ('Separated', 'Separated')],
    )
    RES_WEIGHT = models.CharField(max_length=10)
    RES_EYE_COLOR = models.CharField(max_length=20)
    RES_BLOOD_TYPE = models.CharField(
        max_length=3,
        choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')],
    )
    ORG_ID = models.IntegerField(null=True, blank=True)
    ADD_ID = models.IntegerField()
    RES_ISOWNER = models.CharField(max_length=15, choices=[('Owner', 'Owner'), ('Not Owner', 'Not Owner')])
    RES_ISACTIVE = models.CharField(
        max_length=10, choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE'
    )
    EDUC_ID = models.IntegerField()
    USER_ID = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('RES_LNAME', 'RES_FNAME', 'RES_MNAME')

print(Resident.objects.all())

# Test queries
print(Resident.objects.filter(RES_SEX='Female').count())
print(Resident.objects.filter(ORG_ID=2).count())
print(Resident.objects.filter(RES_AGE__gte=60).count())