
from django.urls import path

from . import views

urlpatterns = [
    # path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    path('',views.demo,name='index'),
    path('mul/',views.multiply,name="multiplication"),


]
