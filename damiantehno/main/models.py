from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class Contact(models.Model):
    first_name = models.CharField(verbose_name='Имя',max_length=15)
    email = models.EmailField(verbose_name='Почта',max_length=150)
    message = models.TextField(verbose_name='Ваше сообщение',max_length=500)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



class Client(models.Model):
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Category(models.Model):
    name = models.CharField('Категория',max_length=30)
    slug = models.SlugField('URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Portfolio(models.Model):
    name = models.CharField('Название', max_length=30)
    image = models.ImageField('Картинка', upload_to='memory')
    slug = models.SlugField('URL', unique=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
