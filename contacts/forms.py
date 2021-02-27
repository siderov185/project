from django.forms import ModelForm
from contacts.models import ContactMessage
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['name', 'family_name', 'mail_address', 'subject', 'message']