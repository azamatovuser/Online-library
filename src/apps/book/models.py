from django.db import models
from apps.account.models import Account

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Book(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    file = models.FileField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title