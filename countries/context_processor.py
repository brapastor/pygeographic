def countries_data(request):
    colombia = {'name': 'colombia', 'code': 'CO'}
    usa = {'name': 'usa', 'code': 'USA'}
    mexico = {'name': 'mexico', 'code': 'MX'}

    countries = [colombia, usa, mexico]

    return {'countries': countries}