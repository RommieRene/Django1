from django.db import models

# Create your models here.

class Logo(models.Model):
    
    name = models.CharField('prosto name',max_length=60)
    img = models.ImageField('Logo Image', upload_to='main_image')

    def __str__(self):

        return self.name

class karusel_possitive(models.Model):

    title = models.CharField('karusel title',max_length=60)
    name = models.CharField('karusel name',max_length=60)
    info = models.TextField('karusel info')
    button_name = models.CharField('karusel button_name',max_length=60)
    img1 = models.ImageField('karusel image1', upload_to='my_images')
    img2 = models.ImageField('karusel image2', upload_to='my_images')
    
    def __str__(self):

        return self.title
    

class karusel(models.Model):

    title = models.CharField('karusel title',max_length=60)
    name = models.CharField('karusel name',max_length=60)
    info = models.TextField('karusel info')
    button_name = models.CharField('karusel button_name',max_length=60)
    img1 = models.ImageField('karusel image1', upload_to='my_images')
    img2 = models.ImageField('karusel image2', upload_to='my_images')
    
    
    def __str__(self):

        return self.title
    
class Contact(models.Model):

    email = models.EmailField('Contact email')
    phone = models.CharField('Contact phone', max_length=40)
    subject = models.CharField('Contact subject',max_length=50)
    message = models.TextField('Contact message')

    def __str__(self):

        return self.email
    
class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    name = models.CharField('SubCategory name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Product(models.Model):

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=80)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='images')
    logo = models.ImageField('Product logo', upload_to='images', blank=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
