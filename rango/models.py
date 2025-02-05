from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    #including __str__() as defined ,  will see <Category: Python> instead of <Category: Category object> if you were to print() the object 
    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)# foreign key, can create one to many relationship with model/table category
    title = models.CharField(max_length=128)#store character data
    url = models.URLField()#store resource URL
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title