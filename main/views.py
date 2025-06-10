from django.shortcuts import render

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
