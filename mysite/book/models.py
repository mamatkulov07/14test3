from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)
    number_of_pages = models.PositiveSmallIntegerField(default=0)
    language = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)


class Member(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    membership_date= models.DateTimeField(auto_now_add=True)
    membership_type = models.CharField(100)


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)


class Fine(models.Model):
    loan_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    paid = models.CharField(max_length=100)


class Reservation(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)