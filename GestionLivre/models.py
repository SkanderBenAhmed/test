
from email.policy import default
from django.db import models
class Author(models.Model):
        firstname=models.CharField(max_length=150, null=False)
        lastname=models.CharField(max_length=150, null=False)
        wikipedia=models.URLField(blank=True)
        def __str__(self) :
              return f"{self.firstname} {self.lastname}"

class Book(models.Model):
      
        
    Aventure="AV"
    Thriller="TR"
    Fantastique="FS"
    Romance="RM"
    Horreur="HR"
    Science_fiction="SF"
    
    GEEKS_CHOICES=[
      (Aventure,"Aventure"), (Thriller,"Thriller"), (Fantastique,"Fantastique"), (Romance,"Romance"), (Horreur,"Horreur"), (Science_fiction,"Science_fiction"),]  
    category=models.CharField(max_length=20,choices=GEEKS_CHOICES)
    stock=models.IntegerField(default=0)
    
    title=models.CharField(max_length=100,null=False)
    price=models.FloatField()
    summary=models.TextField()
    author=models.ForeignKey("author",on_delete=models.CASCADE)
    category =models.CharField(max_length=25, blank=True,choices=GEEKS_CHOICES)
    stock=models.IntegerField(default=0)
    
    def __str__(self):
          return self.title
    
  
    
   
# Create your models here.
