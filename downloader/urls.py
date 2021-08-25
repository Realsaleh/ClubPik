from django.urls import path
from .views import Home


app_name = "downloader"
urlpatterns = [
    path('', Home, name="home"),
]