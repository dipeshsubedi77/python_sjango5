from django.urls import path
from .views import renderRegisterForm

urlpatterns = [
    path('Blog/register',renderRegisterForm)
]