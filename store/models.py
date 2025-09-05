from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

from django.db import models
from category.models import Category
from django.urls import reverse
from django.core.exceptions import ValidationError


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    discription  = models.CharField(max_length=500, blank=True)
    
    price        = models.IntegerField()
    old_price    = models.IntegerField(blank=True, null=True)  # optional

    # Images (min 2, max 5)
    image1 = models.ImageField(upload_to='photos/products',blank=True,null=True)

    image2 = models.ImageField(upload_to='photos/products',blank=True, null=True)

    image3 = models.ImageField(upload_to='photos/products', blank=True, null=True)
    image4 = models.ImageField(upload_to='photos/products', blank=True, null=True)
    image5 = models.ImageField(upload_to='photos/products', blank=True, null=True)

    # Features (min 2, max 5)
    feature1 = models.CharField(max_length=200,blank=True,null=True)
    feature2 = models.CharField(max_length=200,blank=True,null=True)
    feature3 = models.CharField(max_length=200, blank=True, null=True)
    feature4 = models.CharField(max_length=200, blank=True, null=True)
    feature5 = models.CharField(max_length=200, blank=True, null=True)

    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_at  = models.DateTimeField(auto_now=True)

    @property
    def features(self):
        """Return max 3 non-empty features"""
        all_features = [self.feature1, self.feature2, self.feature3, self.feature4, self.feature5]
        return [f for f in all_features if f][:3]

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def clean(self):
        # Validate min 2 images
        if not self.image1 or not self.image2:
            raise ValidationError("At least 2 product images are required.")
        # Validate min 2 features
        if not self.feature1 or not self.feature2:
            raise ValidationError("At least 2 features are required.")

    def __str__(self):
        return self.product_name



class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    # def sizes(self):
    #     return super(VariationManager, self).filter(variation_category='size', is_active=True)




variation_category_choice = (
    ('color','color'),
    # ('size','size'),
)



class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices = variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value