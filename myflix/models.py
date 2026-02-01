from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=50)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    cell_phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Stream(models.Model):
    CATEGORIES = (
        ('F', 'Film'),
        ('S', 'Serie'),
        ('D', 'Documentary')
    )
    code = models.CharField(max_length=10)
    description = models.CharField(blank=False, max_length=100)
    category = models.CharField(blank=False, choices=CATEGORIES, default='F')

    def __str__(self):
        return self.code

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

