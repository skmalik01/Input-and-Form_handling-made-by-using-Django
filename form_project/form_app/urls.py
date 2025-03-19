from django.urls import path
from .views import contact_view, home_view, success_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success')
]
