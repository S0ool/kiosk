from django.db import models


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=100)
    icecream = models.ManyToManyField('IceCream')

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 2
class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Child(models.Model):
    # почему не многие ко многим?
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
