from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="index"),
    path('single_channel/<int:id>/<str:part>', single_channell, name="single"),
    path('listen/<int:user_id>/<int:music_id>', listen_music, name="listen"),
]
