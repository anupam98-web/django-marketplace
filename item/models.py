from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",) # give ordering to the elements 
        verbose_name_plural = 'Categories' # change the default name of the Table

    def __str__(self):
        return self.name # return the original name of the element
    



class Item(models.Model):
    """
    foreign key is connnecting the tables with each other.
    on_delete CASCADE help is deleteing the items depending on the parent table
    is any catergory is deleted the items related to it will also be deleted.
    upload_to help to identify where on the server the images will be uploaded to - Django will create the folder if not created

    """
    category = models.ForeignKey(category, related_name='items', on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_iamges', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # return the original name of the element
