from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def home_view(request):
    return render(request, 'form_app/home.html')

from django.db.utils import IntegrityError

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name'].strip().lower()  
            email = form.cleaned_data['email'].strip().lower()  

            if Contact.objects.filter(name=name, email=email).exists():
                messages.error(request, "Duplicate entry detected. You have already submitted this user data.")
                return redirect('contact')  

            try:
                form.save()  
                messages.success(request, "Form submitted successfully!")  
                return redirect('success')  
            except IntegrityError:
                messages.error(request, "Duplicate data error! Please try again with unique values.")
                return redirect('contact')  

        else:
            messages.error(request, "This file type is not supported.") 
            
    else:
        form = ContactForm()

    return render(request, 'form_app/contact.html', {'form': form})


def success_view(request):
    return render(request, 'form_app/success.html')
