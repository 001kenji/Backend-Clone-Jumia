from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255,null=True)
    number = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=1000,null=True)
    
    def save_model(self,request,obj,form,change):
        #customize the logic before saving the model to harsh the password
        initialpassword = new_password(password)
        print('shed form model is:', initialpassword)
        password(initialpassword)
        
        
        print(password)
        obj.save()
    
    def __str__(self):
        return f"{self.name}  -  {self.email} - {self.number}"
    
    