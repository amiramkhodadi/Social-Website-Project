from django.urls import path,include
from .import views
# from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView , PasswordResetConfirmView
# app_name = 'account'
urlpatterns=[
    ### path('login/' ,views.user_login , name ='login'),
    # path('login/' ,LoginView.as_view() , name ='login'),
    # path('logout/' ,LogoutView.as_view() , name ='logout'),
    # path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-rest/', PasswordResetView.as_view(), name='password_reset'),
    # path('password-rest/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-rest/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]