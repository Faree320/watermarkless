from django.urls import path
from .views import get_routes, video_list, nwm


urlpatterns = [
    path('ronaldo-shorts', nwm),
    # path('', video_list)
]