from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_list, name='table_list'),
    path('tutors', views.tutor_list, name='tutor_list'),
    path('about', views.about, name='about'),
    path('affiliate', views.affiliate, name='affiliate'),
    path('donate', views.donate, name='donate'),
    path('events', views.events, name='events'),
    path('fly_free', views.fly_free, name='fly_free'),
    path('home', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('volunteers', views.volunteer_list, name='volunteer_list'),

    


]