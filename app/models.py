from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    isbn_num = models.CharField(max_length=255)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name