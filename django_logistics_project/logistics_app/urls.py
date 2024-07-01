from django.urls import path
from . import views


urlpatterns = [

    path('', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('index/', views.index_view, name='index_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('ship/', views.ship_view, name='ship_view'),
    path('testimonial/', views.testimonial_view, name='testimonial_view'),

]