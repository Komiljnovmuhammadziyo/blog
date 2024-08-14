from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from users.forms import RegisterForm, UserForm, UserProfileForm
from users.models import CustomUser

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm


class UserCreateView(View):
    def get(self,request):
        register_form = RegisterForm
        messages.info(request,'You have an account now you need login')
        context = {
            'form':register_form
        }

        return render(request, template_name='registration/register.html', context=context)
    def post(self, request):

        create_form = RegisterForm(data= request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login_page' )
        else:
            context = {
                'form':create_form
            }
            return render(request, template_name='registration/register.html', context=context)


class LoginUserView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        # user = request.user
        # user_se_key = request.COOKIES.get('sessionid')
        # print(user.is_authenticated)
        # print(user_se_key)
        context = {
            'form': login_form
        }

        return render(request, template_name='registration/login.html', context=context)
    def post(self, request):

        login_form = AuthenticationForm(data= request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You have been Log In now')
            return redirect('blog:islam-list-view')

        else:
            return render(request, template_name='registration/login.html', context={'form':login_form})


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'profiles/profile.html',{'user': request.user})



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request,'You have been logged out')
        return redirect('blog:islam-list-view')



# class UpdateProfileView(LoginRequiredMixin, View):
#     def get(self, request):
#         userform = UserProfileForm(instance=request.user)
#
#         return render(request, 'profiles/update.html', {'form': userform})
#
#     def post(self, request):
#         user = UserProfileForm(instance=request.user,
#                                  data=request.POST,
#                                  files=request.FILES
#                                  )
#
#         if user.is_valid():
#             user.save()
#             messages.success(request,'Your updates is save !')
#             return redirect('users:profile')
#         return render(request,'profiles/update.html', {'form':user})
