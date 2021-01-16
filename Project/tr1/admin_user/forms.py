from django import forms
from .models import CreateUser


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    re_password = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = CreateUser
        fields = ('username', 'email', 'address',
                  'Designation', 'password', 're_password')

    def clean_password(self):
        print(self.cleaned_data)
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['re_password']
        if len(pass1) < 8:
            raise forms.ValidationError(
                'password is too short. it should be atleast 8 charactor.')

        elif pass1 != pass2:
            raise forms.ValidationError("Passwords don't match.")
        return pass1, pass2


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username:', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(max_length=100, label='Enter Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ('username', 'email')
