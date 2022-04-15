from django.shortcuts import render
from .models import Contact, Client, Category, Portfolio
from .forms import ContactForm, ClientForm
import telebot

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        phone_form = ClientForm(request.POST)
        if form.is_valid():
            message = f'{request.POST["first_name"]}\n{request.POST["email"]}\n{request.POST["message"]}'
            bot = telebot.TeleBot('5070793905:AAFgZPzVkYG1V_J2uAc3bYvr-f9KB6RvQvw')
            try:
                bot.send_message(5032493900, message)
            except:
                pass
            form.save()
        elif phone_form.is_valid():
            message = f'По номеру телефона:  {request.POST["phone"]}'
            bot = telebot.TeleBot('5070793905:AAFgZPzVkYG1V_J2uAc3bYvr-f9KB6RvQvw')
            try:
                bot.send_message(5032493900, message)
            except:
                pass
            phone_form.save()

    form = ContactForm()
    phone_form = ClientForm()
    contacts = Contact.objects.all()
    contacts_1 = Client.objects.all()
    content = {
        'contacts': contacts,
        'contacts_1': contacts_1,
        'form': form,
        'phone_form': phone_form,
        'category': Category.objects.all(),
        'portfolio': Portfolio.objects.all(),
    }
    return render(request, 'main/index.html', content)



# Create your views here.
