from django.urls import path
from . import views


urlpatterns = [
       path('api/Employee/', views.Item,name='Employee'),
]
