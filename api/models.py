from django.db import models

# Create your models here.

class Company(models.Model) :
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('NON IT', 'NON IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    

class Employee(models.Model) :
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=(('SDE', 'softwareDeveloper'), ('Hr', 'HR'), ('Salesman', 'Salesman'), ('Intern', 'Intern')))
    salary = models.CharField(max_length=8)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
