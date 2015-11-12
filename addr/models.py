from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=20,primary_key=True)
    Name=models.CharField(max_length=40)
    Age=models.IntegerField(max_length=40)
    Country=models.CharField(max_length=50)
        
    def __unicode(self):
        return self.Name

class Book(models.Model):
    ISBN = models.CharField(max_length=20,primary_key=True)
    Title= models.CharField(max_length=20) 
    Authors = models.ForeignKey(Author,related_name='person_book')
    Publisher=models.CharField(max_length=20)
    PublishDate=models.DateField()
    Price=models.CharField(max_length=20)
    
    def __unicode(self):
        return self.Title