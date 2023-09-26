from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
import datetime
from django.urls import reverse
from main.models import Item
from django.core import serializers
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    # Mengambil data dari model dan menghitung jumlah itemnya
    item_count = Item.objects.filter(user=request.user).count()

    context = {
        'appl_name': 'Seven Siege',
        'name': request.user.username,
        'class': 'PBP B',
        'items': items,
        'item_count': item_count,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_html(request):
    data = Item.objects.all().values()
    return HttpResponse(data)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request, item_id):
    if request.method == 'POST' and 'Increment' in request.POST:
        item = Item.objects.get(id=item_id)
        item.amount += 1
        item.save()
    return redirect('/')

def subtract_amount(request, item_id):
    if request.method == 'POST' and 'Decrement' in request.POST:
        item = Item.objects.get(id=item_id)
        item.amount = max(item.amount - 1, 0)
        item.save()
    return redirect('/')

def remove_item(request, item_id):
    if request.method == 'POST' and 'Remove' in request.POST:
        item = Item.objects.get(id=item_id)
        item.delete()
    return redirect('/')