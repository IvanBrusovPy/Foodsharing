import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from share_service.forms import NewCustomerForm, NewCafeForm, NewOfferForm
from share_service.models import Cafe, City, Offer, Customer, Order
from django.utils import timezone


def register_user(request):
    if request.method == "POST":
        if request.POST.get('user_type') == 'customer':
            form = NewCustomerForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(reverse('user_home'))
            else:
                return render(request, "login.html", {"city_list": City.objects.all().values()})
        if request.POST.get('user_type') == 'manager':
            form = NewCafeForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(reverse('cafe_home'))
            else:
                return render(request, "login.html", {"city_list": City.objects.all().values()})
    else:
        return render(request, "login.html", {"city_list": City.objects.all().values()})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            manager = Cafe.objects.filter(user=user)
            if manager:
                return HttpResponseRedirect(reverse('cafe_home'))
            else:
                return HttpResponseRedirect(reverse('user_home'))
        else:
            return render(request, "login.html", {"error_message": "sign_in", "city_list": City.objects.all().values()})
    else:
        return render(request, "login.html", {"city_list": City.objects.all().values()})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required()
def user_home(request):
    today = datetime.date.today()
    user = request.user
    user_city = Customer.objects.get(user__username=user.username).city
    offers = Offer.objects.filter(cafe__city=user_city, quantity__gte=1, created_at__gte=today)
    orders = Order.objects.filter(customer__user=user, offer__created_at__gte=today).exclude(status__exact="Picked")
    city_list = City.objects.all().exclude(name=user_city.name)
    return render(request, "user_home.html", {"user_name": user.first_name, "offers": offers,
                                              "user_city": user_city, "city_list": city_list, "orders": orders})


@login_required()
def cafe_home(request):
    today = datetime.date.today()
    cafe_name = request.user.first_name
    cafe = Cafe.objects.get(user=request.user)
    offers = Offer.objects.filter(cafe=cafe, created_at__gte=today)
    orders = Order.objects.filter(offer__cafe=cafe, offer__created_at__gte=today).exclude(status__exact="Picked")
    return render(request, "cafe_home.html", {"cafe_name": cafe_name, "offers": offers, "orders": orders})


@login_required()
def filter_city(request):
    if request.method == "POST":
        city = request.POST.get('city')
        today = datetime.date.today()
        user_name = request.user.first_name
        user_city = City.objects.get(pk=city)
        offers = Offer.objects.filter(cafe__city=user_city, quantity__gte=1, created_at__gte=today)
        city_list = City.objects.all().exclude(name=user_city.name)
        orders = Order.objects.filter(customer__user__first_name=user_name, offer__created_at__gte=today).exclude(status__exact="Picked")
        return render(request, "user_home.html", {"user_name": user_name, "offers": offers,
                                                  "user_city": user_city, "city_list": city_list, "orders": orders})


@login_required()
def create_offer(request):
    cafe = Cafe.objects.get(user=request.user)
    if request.method == "POST":
        form = NewOfferForm(request.POST)
        if form.is_valid():
            form.save(cafe)
            return HttpResponseRedirect(reverse('cafe_home'))
        else:
            return HttpResponse("Error")


@login_required()
def create_order(request):
    if request.method == 'POST':
        quantity = request.POST.get('order_quantity')
        offer_id = request.POST.get('offer_id')
        offer = Offer.objects.get(id=offer_id)
        customer = Customer.objects.get(user=request.user)
        Order.objects.create(quantity=quantity, offer=offer, customer=customer)
        offer.quantity -= int(quantity)
        offer.save()
        return HttpResponseRedirect(reverse('user_home'))
    else:
        return HttpResponseRedirect(reverse('user_home'))


@login_required()
def pick_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(pk=order_id)
        order.status = "Picked"
        order.save()
        return HttpResponseRedirect(reverse('user_home'))


@login_required()
def pack_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.status = "Ready"
        order.save()
        return HttpResponseRedirect(reverse('cafe_home'))
