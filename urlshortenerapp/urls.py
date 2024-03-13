from django.urls import path
from urlshortenerapp import views
urlpatterns = [
  
    path('',views.index,name='index')
    
]