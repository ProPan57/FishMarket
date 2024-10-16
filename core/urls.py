from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',          views.index,     name='index'),
    path('about',     views.about,     name='about'),
    path('cart',      views.cart,      name='cart'),
    path('events',    views.events,    name='events'),
    path('shop',      views.shop,      name='shop'),
    path('fish',      views.fish,      name='fish'),
    path('loyalty',   views.loyalty,   name='loyalty'),

]