from django.db.models.fields import CharField
from core.settings import DEBUG
from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
  title = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
    return self.title



class Book(models.Model):
  title = models.CharField(max_length= 100)
  category = models.ForeignKey(Category,related_name= "books",on_delete= models.CASCADE)
  author = models.CharField(max_length=100,default='arshameenu')
  isbn = models.CharField(max_length=50)
  pages =models.IntegerField()
  price = models.IntegerField()
  stock = models.IntegerField()
  description = models.TextField()
  imageUrl = models.URLField()
  status = models.BooleanField(default= True)
  date_created = models.DateField(auto_now_add= True)

  class Meta:
    ordering = ['-date_created']

  def __str__(self):
    return self.title
 
class Product(models.Model):
  product_tag = models.CharField(max_length=10)
  name = models.CharField(max_length= 100)
  category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
  price = models.IntegerField()
  quantity = models.IntegerField()
  description =models.TextField()
  stock = models.CharField(max_length=100)
  imageUrl = models.URLField()
  status = models.BooleanField(default= True)
  date_created = models.DateField(auto_now_add= True)


  class Meta:
    ordering = ['-date_created']

  def __str__(self):
    return '{} {}'.format(self.product_tag,self.name)




