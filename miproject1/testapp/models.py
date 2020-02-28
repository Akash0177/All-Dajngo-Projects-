from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ContactInfo):
    subject=models.CharField(max_length=128)
    salary=models.FloatField()

class ContactInfo1(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=256)

class Student1(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher1(ContactInfo):
    subject=models.CharField(max_length=128)
    salary=models.FloatField()

class Parent(models.Model):
    fd1=models.CharField(max_length=128)
    fd2=models.CharField(max_length=128)

class Child(Parent):
    fd3=models.CharField(max_length=128)
    fd4=models.CharField(max_length=128)

class SubChild(Child):
    fd5=models.CharField(max_length=128)
