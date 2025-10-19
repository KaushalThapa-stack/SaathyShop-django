from django.shortcuts import render

from store.models import Product
from slider.models import SliderImage
from store.models import ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available = True).order_by('created_date')
    slider_images = SliderImage.objects.all()[:5]

        # GET reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id = product.id, status = True)

    context = {
        'products' : products,
        'slider_images': slider_images,
        'reviews': reviews,
    }

    return render (request, 'home.html',context)
