from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    email = models.TextField()
    description = models.TextField()
    visit_date = models.DateField()


    objects = models.Manager()

    def __str__(self):
        return self.name

class Query(models.Model):
    name = models.CharField(max_length=20)
    subject = models.TextField()
    email = models.TextField()
    message = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.email

class DoctorID(models.Model):
    doctor_identifier = models.IntegerField(primary_key=True)

    class Meta:
        managed = True

    objects = models.Manager()
    def __str__(self):
        return self.doctor_identifier
