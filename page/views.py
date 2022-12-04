from django.shortcuts import render
from .models import cars
from .forms import ComplaintForm


def home(request):
    return render(request, 'allcars.html')
    
def offers(request):
    return render(request, 'offers.html')

def about_us(request):
    return render(request, 'about-us.html')

def teams(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def car_list(request):
    car=cars.objects.all()
    context = {
        'car':car,
    }
    return render(request, 'fleet.html', context)

def details(request, id):
    car=cars.objects.get(id=id)
    context = {
        'car':car,
    }
    return render(request, 'car_details.html', context)

def complaints(request):
    form = ComplaintForm()
    if request.method=="POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)

def blog_details(request):
    return render(request, 'blog-details.html')

