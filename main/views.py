from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'appl_name': 'Seven Siege',
        'name': 'Muhammad Raihan Akbar',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)