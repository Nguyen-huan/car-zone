from django.shortcuts import render
from .models import Team
from cars.models import Car
import os


# Create your views here.
def home(request):
    # print("file tuong doi", __file__)
    # print("file tuyet doi", os.path.abspath(__file__))
    # print("file cha 1", os.path.dirname(os.path.abspath(__file__)))
    # print("file cha 1", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    print(type(request.user))
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, "pages/home.html", data)


def contact(request):
    return render(request, "pages/contact.html")


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, "pages/about.html", data)


def services(request):
    return render(request, "pages/services.html")
