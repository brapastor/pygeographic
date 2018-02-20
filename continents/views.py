from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ContinentsView(TemplateView):
    template_name = 'continents/continents.html'

    def get_context_data(self, *args, **kwargs):
        america = {
            'name': 'America',
            'translation': 'america',
            'color': '#000'
           }

        africa = {
            'name': 'Africa',
            'translation': 'Africa',
            'color': '#F04261'
        }

        asia = {
            'name': 'asia',
            'translation': 'asia',
            'color': '#ee65ee'
        }

        oceania = {
            'name': 'oceania',
            'translation': 'oceania',
            'color': '#ee65dd'
        }

        continents =[america, africa, asia, oceania]

        return {'continents': continents}
