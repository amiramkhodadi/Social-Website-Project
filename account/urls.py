from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'account'
urlpatterns=[
    # path('login/' ,views.user_login , name ='login'),
    path('login/' ,LoginView.as_view() , name ='login'),
    path('logout/' ,LogoutView.as_view() , name ='logout'),
    path('', views.dashboard, name='dashboard'),
]