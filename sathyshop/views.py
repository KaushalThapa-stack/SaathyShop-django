from django.shortcuts import render

from store.models import Product
from slider.models import SliderImage

def home(request):
    products = Product.objects.all().filter(is_available = True)
    slider_images = SliderImage.objects.all()[:5]

    context = {
        'products' : products,
        'slider_images': slider_images,
    }

    return render (request, 'home.html',context)
