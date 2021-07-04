from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<int:num>/', views.resto_detail),
    # path('resto/<int:num>/', views.resto),
    # path(r'^restro/$', views.Restro.as_view()),
]