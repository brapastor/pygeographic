from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = "countries/home.html"

    # def get_context_data(self, *args, **kwargs):
    #     colombia = {'name': 'colombia', 'code': 'CO'}
    #     usa = {'name': 'usa', 'code': 'USA'}
    #     mexico = {'name': 'mexico', 'code': 'MX'}
    #
    #     countries = [colombia, usa, mexico]
    #
    #     return {'countries': countries}

    # ESTA SE LLAMA CON EL VIEW :from django.views.generic import VIEW

    # def get(self, request, *args, **kwargs):
    #     return render(request, "countries/home.html")


# VISTA BASADA EN FUNCIONES

# def home(request):
#     return render(request, "countries/home.html")


class TagsView(TemplateView):
    template_name = 'countries/tags.html'
