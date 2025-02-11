from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    Name_Max_Length =128
    name = models.CharField(max_length=Name_Max_Length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True) # slugfield is unique (Django and django is different)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        #slugify replaces whitespace with hyphens , circumnavigating the percent-encoded problem
        #overidden save method calls parent save method in base django.db.models.Model
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    #including __str__() as defined ,  will see <Category: Python> instead of <Category: Category object> if you were to print() the object 
    
class Page(models.Model):
    Title_Max_Length =128
    Url_Max_Length = 200
    category = models.ForeignKey(Category, on_delete=models.CASCADE)# foreign key, can create one to many relationship with model/table category
    title = models.CharField(max_length=Title_Max_Length)#store character data
    url = models.URLField()#store resource URL
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title