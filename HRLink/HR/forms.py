import email

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Employee
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import authenticate
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=40, help_text="Required, a valid email must be entered"
    )

    class Meta:
        model = Account
        fields = (
            "email",
            "username",
            "password1",
            "password2",
            "accId",
            "availableVac",
            "phone",
            "DOB",
        )


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    # runs first thing in the form
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login Credentials")


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(
        label=("email"),
        widget=forms.EmailInput(attrs={"required": True, "autofocus": True}),
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        Email = self.cleaned_data.get("email")

        password = self.cleaned_data.get("password")

        if Email is not None and password:
            self.user_cache = authenticate(self.request, Email=email, password=password)
        if self.user_cache is None:
            raise self.get_invalid_login_error()
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data





class AddForm(ModelForm):
    gender_choices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = forms.ChoiceField(
         widget=forms.widgets.RadioSelect(attrs={}),choices=gender_choices,)
    

    class Meta:
        model = Employee
        fields = (
            "Name",
            "accId",
            "email",
            "address",
            "phone",
            "gender",
            "availableVac",
            "salary",
            "Birth_date",
        )
        widgets = {
            "Birth_date": forms.widgets.DateInput(  # date
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "class": "form-group",
                }
            ),
            'email' : forms.widgets.EmailInput(
                attrs={
                    'type':"email",
                    "placeholder" : "Enter your email",
                }
            )
        
        }


