from django.urls import path
from .views import nwm, get_routes


urlpatterns = [
    path('', get_routes),
    path('ronaldo-shorts', nwm),
]