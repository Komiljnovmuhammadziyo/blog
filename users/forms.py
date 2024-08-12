from django import forms

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email','image','password']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email','password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
