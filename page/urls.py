from django.urls import path
from .views import *
from .forms import ComplaintForm


urlpatterns =[
    path('home/', home, name= 'home'),
    path('about-us/', about_us, name= 'about-us'),
    path('contact-us/', contact, name= 'contact-us'),
    path('allcars/', car_list, name='allcars'),
    path('more/cars/', offers, name= 'offers'),
    path('teams/', teams, name= 'teams'),
    path('testimonial/', testimonials, name='testimonials'),
    path('blog/', blog, name='blog'),
    path('terms/', terms, name= 'terms'),
    path('blog/details/', blog_details, name= 'blog-details'),
    path('car/<int:id>/car/details/', details, name='car-details'),
    path('car/create/', complaints, name='create_cars'),
    #path('<int:id>car/delete/', delete, name='delete_cars'),
    
]