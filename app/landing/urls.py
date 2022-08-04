from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="landing-home"),
    path('pgp', views.pgp, name="pgp-view ")
]
