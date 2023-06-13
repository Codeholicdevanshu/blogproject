from django.db import models
import datetime

# User registration Model
class Register(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    @staticmethod
    def get_user_by_email(email=email):
        try:
            return Register.objects.get(email=email)
        except:
            return False
        
        

    
    
#blog Model
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    discription = models.TextField(max_length=100,null=False,default='')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
