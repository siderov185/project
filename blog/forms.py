from django import forms

class Contacts(forms.Contacts):
    name = forms.CharField(label='Вашето име', max_length=50)
    email = forms.EmailField(label='Вашият Email')
    description = forms.CharField(label='Тема', max_length=50)
    text = forms.TextField(label='Вашето съобщение')