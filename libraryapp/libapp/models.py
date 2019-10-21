from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):

    author_name = models.CharField(max_length=200)
    # about_author = models.TextField(blank=True, null=True,help_test='my first testing')

    def __str__(self):
        return self.author_name

    def get_author(self):
        return self.author_name

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    isbn = models.CharField(max_length=200)
    stock = models.IntegerField()
    available1 = models.IntegerField()
    author_name = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.book_name

class Member(models.Model):
    member_id = models.IntegerField()
    member_name=models.CharField(max_length=200)
    member_address=models.CharField(max_length=200)


    def __str__(self):
        return self.member_name

class Record(models.Model):
    book_issue_date=models.DateField()
    book_return_date=models.DateField()
    author_name=models.ForeignKey(Author,null=True, on_delete=models.CASCADE)
    book_name=models.ForeignKey(Book,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.book_name.book_name


@receiver(post_save,sender=Record)
def upadate_stock(sender,instance,**kwargs):
    stock1=instance.book_name.available1
    if stock1>0:

        stock1=stock1-1
        book1 = instance.book_name
        instance.book_name.available1=stock1
        book1.save()
    return True
