from django.db import models

# Create your models here.
from django.db import models
from  django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator



    
class Review(models.Model):
    name = models.CharField(max_length=32, validators=[MinLengthValidator(3)])
    hotel_detail = models.CharField(max_length=500, validators=[MinLengthValidator(3)] )    
    review = models.CharField(max_length=512, validators=[MinLengthValidator(16)] )
    rev_stars = models.IntegerField( validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='pics/%y/%m/%d/',null=True, blank=True, verbose_name='image')
    created_at = models.DateTimeField( default=timezone.now)

    class Meta:
        ordering = ["created_at"]


