from django.urls import path
from .views import nwm


urlpatterns = [
    path('ronaldo-shorts', nwm),
    # path('', video_list)
]