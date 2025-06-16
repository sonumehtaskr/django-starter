from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    context = {
        'projects': [
            {'title': 'Portfolio Website', 'description': 'A personal portfolio built with Django and Tailwind.', 'link': 'https://your-portfolio.com'},
            {'title': 'Weather App', 'description': 'A weather forecasting app using external APIs.', 'link': '#'},
        ]
    }
    return render(request, 'main/projects.html', context)

def contact(request):
    return render(request, 'main/contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})
