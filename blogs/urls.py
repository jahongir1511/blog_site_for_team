from django.urls import path
from .views import get_home


app_name = 'blogs'
urlpatterns = [
    path('', get_home, name='home')
]