from django.urls import path
from .views import get_routes, video_list


urlpatterns = [
    path('', get_routes),
    # path('', video_list)
]