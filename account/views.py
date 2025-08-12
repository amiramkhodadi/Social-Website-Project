from django.shortcuts import render
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile

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




def register(request):
    if request.method == "POST" :
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            instance = user_form.save(commit=False)
            instance.set_password(
                user_form.cleaned_data['password']
            )
            instance.save()
            Profile.objects.create(user=instance)
            return render(request , 'account/register_done.html' , {'instance' : instance})
    else :
        user_form = UserRegistrationForm()

    return render(request , 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST' :
        user_form = UserEditForm(data=request.POST , instance = request.user )
        profile_form= ProfileEditForm(data=request.POST , instance = request.user.profile, files = request.FILES )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})