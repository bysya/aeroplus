from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=64, null=True)
    data = models.DateField()
    adres = models.CharField(max_length=64)
    responsible = models.CharField(max_length=64)
    foto = models.ImageField(upload_to="images/")
    warranty = models.FileField()
    service = models.FileField()
    file = models.FileField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=64)
    phone = models.IntegerField()
    obj = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, related_name="obj")
    