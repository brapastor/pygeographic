from django.urls import reverse

def countries_data(request):
    colombia = {'name': 'colombia', 'code': 'CO', 'id': 1, 'detail_url': reverse("countries:country_id_detail", kwargs={'id':1})}
    usa = {'name': 'usa', 'code': 'USA', 'id': 2, 'detail_url': reverse("countries:country_id_detail", kwargs={'id':2})}
    mexico = {'name': 'mexico', 'code': 'MX', 'id': 3, 'detail_url': reverse("countries:country_id_detail", kwargs={'id':3})}

    countries = [colombia, usa, mexico]

    return {'countries': countries}