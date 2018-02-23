from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Country


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


class CountryDetailView(TemplateView):
    template_name = "countries/country_detail.html"

    def get_context_data(self, *args, **kwargs):
        code = kwargs['code']
        return {'code': code}


class CountryDetailIDView(TemplateView):
    template_name = "countries/country_id_detail.html"

    def get_context_data(self, *args, **kwargs):
        code_id = kwargs['id']
        country = get_object_or_404(Country, id=code_id)
        # try:
        #     country = Country.objects.get(id=code_id)
        # except Country.DoesNotExist:
        #     raise Http404()
        return {'country': country}


class CountrySearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    # context_object_name = 'countries

    def get_queryset(self):
        # CON LAS kwargs SE OBTIENE EL PARAMETRO DE LA URLS
        query = self.kwargs['query']

        # io = [1, 2, 3]

        return Country.objects.filter(name__contains=query)
        # return Country.objects.filter(id__in=io)
        # return Country.objects.filter(continent__name__contains='africa')
        # return Country.objects.filter(name__startswith='ar')
