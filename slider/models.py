from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_max_images():
    """Custom validation to limit total number of images."""
    from .models import SliderImage
    if SliderImage.objects.count() >= 5:
        raise ValidationError("You can only upload a maximum of 5 images.")

class SliderImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='slider/')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Limit to 5 images
        if not self.pk and SliderImage.objects.count() >= 5:
            raise ValidationError("You can only have 5 slider images.")

    def __str__(self):
        return self.title if self.title else f"Slider Image {self.id}"
