
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "This email is already registered."
            )

        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if password:
            if len(password) <= 8:
                raise forms.ValidationError(
                    "Password must contain more than 8 characters."
                )

            if not any(c.isupper() for c in password):
                raise forms.ValidationError(
                    "Password must contain an uppercase letter."
                )

            if not any(c.islower() for c in password):
                raise forms.ValidationError(
                    "Password must contain a lowercase letter."
                )

            if not any(not c.isalnum() for c in password):
                raise forms.ValidationError(
                    "Password must contain a special character."
                )

        return password
