from django.shortcuts import render

from store.models import Product
from slider.models import SliderImage

def home(request):
    products = Product.objects.all().filter(is_available = True)
    # Only include slider images with existing files to avoid blank slides
    valid_slider_images = []
    for si in SliderImage.objects.all():
        try:
            if si.image and si.image.name and si.image.storage.exists(si.image.name):
                valid_slider_images.append(si)
        except Exception:
            # Skip any entries that error while checking storage
            continue
    slider_images = valid_slider_images[:5]

    context = {
        'products' : products,
        'slider_images': slider_images,
    }

    return render (request, 'home.html',context)
