from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def home_view(request):
    return render(request, 'form_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = ContactForm()

    return render(request, 'form_app/contact.html', {'form': form})

def success_view(request):
    return render(request, 'form_app/success.html')
