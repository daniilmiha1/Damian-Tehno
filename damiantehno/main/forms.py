from django import forms
from .models import Contact, Client
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        #fields = ['name', 'email', 'message']
        fields = '__all__'
        widgets = {
            #<textarea name="message" id="message" class="form-control" rows="4" placeholder="Message" required></textarea>
            'first_name': forms.TextInput(
                    attrs={
                        'id': 'name',
                        'class': 'form-control',
                        'placeholder': 'Имя',
                    }
            ),
            'email': forms.EmailInput(
                    attrs={
                        'id': 'email',
                        'class': 'form-control',
                        'placeholder': 'Почта',
                    }
            ),
            'message': forms.Textarea(
                    attrs={
                        'id': 'message',
                        'class': 'form-control',
                        'placeholder': 'Ваше сообщение или заказ',
                        'rows': '5'
                    }
            )
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone']
        phone = PhoneNumberField()
