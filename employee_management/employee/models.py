from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile_Number= models.CharField(max_length=15)
    select_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    select_dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Allcate_Reporting_Manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    Date_of_joining = models.DateField()
    username = models.CharField(max_length=100)
    Set_password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
