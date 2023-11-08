from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("user_home/", views.user_home, name="user_home"),
    path("cafe_home/", views.cafe_home, name="cafe_home"),
    path("create_offer/", views.create_offer, name="create_offer"),
    path("filter_city/", views.filter_city, name="filter_city"),
    path("create_order/", views.create_order, name="create_order"),
    path("pick_order/", views.pick_order, name="pick_order"),
    path("pack_order/", views.pack_order, name="pack_order"),

]
