from django.db import models
from datetime import date


class FoodCategory(models.Model):
    Name=models.CharField(max_length=30)
    def __str__(self):
        return self.Name
    

class Food(models.Model):
   FoodName=models.CharField(max_length=30)
   FCategory=models.ForeignKey(FoodCategory,on_delete=models.PROTECT)
   Description=models.TextField()
   Size=models.CharField(choices=[('1','one person'),('2','two person'),('3','family')],max_length=2)
   Price=models.IntegerField()
   ImageFood=models.ImageField(upload_to='Images')
   PreparationTime=models.SmallIntegerField(help_text='please enter time based on minutes')
   SpecialFood=models.BooleanField(default=False)
   def __str__(self):
        return self.FoodName
   

class ReserveTable(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=11) 
    Email=models.EmailField(blank=True) 
    ReserveDate=models.DateField(default=date.today())  
    ReserveTime=models.TimeField(null=True)  
    NoOfPeople=models.SmallIntegerField()
    
    
