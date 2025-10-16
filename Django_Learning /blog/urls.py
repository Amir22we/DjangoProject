from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, kwargs={"name": "Tom", "age": 38}),
    path('contact/', views.contact),
    path('user/<str:name>/<int:age>/', views.user),
    path('user/<str:name>/', views.user),
    path('user/', views.user),
    path('winner/<str:name>/<int:price>/', views.winner),
    path('winner/<str:name>/', views.winner),
    path('winner/', views.winner),
]