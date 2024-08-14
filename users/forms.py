from django import forms

from users.models import CustomUser


from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'image','password')

    def save(self, commit=True):

        user = super().save(commit)

        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email','password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
