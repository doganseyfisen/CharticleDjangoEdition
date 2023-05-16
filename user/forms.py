from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords are not matching.")
        
        values = {
            "username": username,
            "password": password,
        }
        
        return values

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label = "Username")
    password = forms.CharField(label = "Password", widget=forms.PasswordInput)