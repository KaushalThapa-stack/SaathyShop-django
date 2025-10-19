from .models import SliderImage

def hom(request):
    slider_images = SliderImage.objects.all()[:5]
    return render(request, 'home.html', {'slider_images': slider_images})
