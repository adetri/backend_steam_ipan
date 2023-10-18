from django.db import models

# Create your models here.


class Karyawan(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="", unique=True)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)

    def __str__(self):
        return "id: ({}) nama:({}) ".format(self.id, self.name)


class Role(models.Model):
    name = models.CharField(max_length=10)
    level = models.SmallIntegerField(unique=True)

    def __str__(self):
        return "id: ({}) nama:({}) ".format(self.id, self.name)
