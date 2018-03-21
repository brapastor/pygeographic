from django import forms
from countries.models import Country
from people.models import Person


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first name')
    nationality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
    father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())
    # date = forms.DateField()
    # active = forms.BooleanField()
    # email = forms.EmailField()


class RegisterFormModel(forms.ModelForm):

    def __init__(self, fathers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['father'].queryset = fathers

    class Meta:
        model = Person
        fields = ['first_name', 'nationality', 'father']
