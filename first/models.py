from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Contact(models.Model):
#     phone_number = models.CharField(max_length=32)
#     address = models.CharField(max_length=100)
#     email = models.EmailField()


class auth_user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    username = models.CharField(max_length=25, )
    email = models.EmailField(max_length=254)



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    todo_name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return self.todo_name + 'created by' + self.user.username