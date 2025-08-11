from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# from django.contrib.auth.views  import LoginView,LogoutView
# Create your views here.
# def user_login(request):
#     if request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username , password = password)
#             if user :
#
#                 if user.is_active :
#                     login(request,user)
#                     return HttpResponse("YOU ARE LOGIN ;) ")
#                 else:
#                     return HttpResponse("YOU ARE Dissabled ;) ")
#             else :
#                 return HttpResponse("YOU ARE  NOT REGISTER YET ;) ")
#
#         else :
#             return HttpResponse("invalid data in form input")
#
#     else :
#         form = LoginForm()
#
#     return render(request , 'account/login.html' , {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request , 'account/dashboard.html' , {'section' : 'dashboard'})


