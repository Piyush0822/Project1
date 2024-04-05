from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=128)  # Storing hashed passwords
    # date_of_birth = models.DateField(blank=True, null=True)
    # phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.name



class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    

    def __str__(self):
        return self.full_name
    













    # def __str__(self):
    #     return self.name + "("+self.email+")"

    # def check_passwords(self):
    #     if self.password1 == "" or self.password2 == "":
    #         return False
    #     elif self.password1 != self.password2:
    #         return False
    #     else:
    #         return True