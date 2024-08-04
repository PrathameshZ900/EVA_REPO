from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # other fields ...

    groups = models.ManyToManyField(
        Group,
        related_name='books_library_user_set',  # Unique related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='books_library_user_permissions_set',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=150)
    birthdate = models.DateField(blank=True,null=True)
    biography = models.CharField( max_length=250,blank=True,null=True)




    def __str__(self):
        return self.name



class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True,blank=True,related_name='Author')
    published_date =  models.DateField()
    isbn = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()


    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50,unique=True)