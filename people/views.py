from django.http import JsonResponse
from django.shortcuts import render
from people.forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        return JsonResponse(form.cleaned_data)

    return render(request, "people/register.html", {'form': form})


