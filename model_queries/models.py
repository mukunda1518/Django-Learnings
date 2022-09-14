from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


class UserParent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)


class Musician(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    instrument = models.CharField(max_length=100, null=True, blank=True)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    num_stars = models.IntegerField(null=True, blank=True)


class Person(models.Model):
    name = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, blank=True)
    invite_reason = models.CharField(max_length=64, null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(null=True, blank=True)


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)



