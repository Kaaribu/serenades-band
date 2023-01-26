from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.


class NewUserForm(UserCreationForm):
    """
    NewUserForm is a subclass of Django's built-in UserCreationForm, with additional fields specific to creating a user
    for a music band website.

    Attributes:
    - username: the username of the user
    - fullname: the full name of the user
    - email: the email of the user
    - password1: the password of the user
    - password2: the password of the user, repeated

    Methods:
    - save(commit=True): Saves the form and creates a new user.
    """
    fullname = forms.CharField(max_length=100, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ("username", "fullname", "email", "password1", "password2")

    # change field text color to red
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'fullname', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''

        self.fields['fullname'].widget.attrs['class'] = 'form-control'
        self.fields['fullname'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['fullname'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''

        self.fields['username'].widget.attrs['style'] = 'color: black;'
        self.fields['fullname'].widget.attrs['style'] = 'color: black;'
        self.fields['email'].widget.attrs['style'] = 'color: black;'
        self.fields['password1'].widget.attrs['style'] = 'color: black;'
        self.fields['password2'].widget.attrs['style'] = 'color: black;'

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password")
            if not user.check_password(password):
                raise forms.ValidationError("Invalid username or password")
            if not user.is_active:
                raise forms.ValidationError("Account is not active")
        return super(LoginForm, self).clean()

    # change field text color to red
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs['style'] = 'color: black;'
        self.fields['password'].widget.attrs['style'] = 'color: black;'

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text='Required')
    email = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(max_length=300, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ("name", "email", "message")

    # change field text color to red
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for fieldname in ['name', 'email', 'message']:
            self.fields[fieldname].help_text = None


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required')
    email = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2000)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "message")

    # change field text color to red
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for fieldname in ['first_name', 'last_name', 'email', 'message']:
            self.fields[fieldname].help_text = None

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['message'].label = ''

















