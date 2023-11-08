from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from share_service.models import Customer, Cafe, City, Offer


class NewCustomerForm(UserCreationForm):
    phone = forms.CharField(required=True)
    user_city = forms.CharField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2", "user_city", "first_name")

    def save(self):
        user = super(NewCustomerForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.save()
        city = City.objects.filter(name=self.cleaned_data['user_city']).first()
        Customer.objects.create(city=city,
                                phone=self.cleaned_data['phone'], user=user)
        return user


class NewCafeForm(UserCreationForm):
    phone = forms.CharField(required=True)
    city = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    cafe_address = forms.CharField(required=True)
    cafe_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2", "city", "first_name", "cafe_address",
                  "cafe_name")

    def save(self):
        user = super(NewCafeForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.save()
        if City.objects.filter(name=self.cleaned_data['city']):
            city = City.objects.filter(name=self.cleaned_data['city']).first()
        else:
            city = City.objects.create(name=self.cleaned_data['city'])

        Cafe.objects.create(name=self.cleaned_data['cafe_name'], city=city,
                            address=self.cleaned_data['cafe_address'],
                            phone=self.cleaned_data['phone'], user=user)
        return user


class NewOfferForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    book_time = forms.TimeField(required=True)
    pick_up_time = forms.TimeField(required=True)
    price = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = Offer
        fields = ("name", "description", "book_time", "pick_up_time", "price", "quantity")

    def save(self, cafe):
        Offer.objects.create(name=self.cleaned_data['name'], cafe=cafe,
                             description=self.cleaned_data['description'],
                             book_time=self.cleaned_data['book_time'],
                             pick_up_time=self.cleaned_data['pick_up_time'],
                             price=self.cleaned_data['price'],quantity=self.cleaned_data['quantity'] )


