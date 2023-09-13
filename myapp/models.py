from django.db import models
from django.contrib.auth.models import User
from datetime import date
from PIL import Image

class Category_goods(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

# class Instance(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Products(models.Model):
    title = models.CharField(max_length=200)
    price= models.FloatField()
    discount_price = models.FloatField()
    Category_goods = models.ForeignKey('Category_goods', on_delete=models.SET_NULL, null=True, related_name='Category_goods')
    description= models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products_Review(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE, null=True, blank=True)
    reviewer = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=200)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="profile_pics/default.png",upload_to="profile_pics")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_image.path)
        if img.height >300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)