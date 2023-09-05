from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register/contact-success.html')
    else:
        form = ContactForm()

    return render(request, 'register/contact.html', {'form': form})