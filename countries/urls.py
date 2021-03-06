from django.urls import path
from countries.views import (
    CountryDetailView,
    CountryDetailIDView,
    CountrySearchView
)
app_name = 'countries'

urlpatterns = [
    path("search/<query>", CountrySearchView.as_view(), name="country_search"),
    path("<int:pk>/", CountryDetailIDView.as_view(), name="country_id_detail"),
    path("<code>/", CountryDetailView.as_view(), name="country_code_detail")
]