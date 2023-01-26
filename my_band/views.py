from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from my_band.form import NewUserForm, LoginForm, OrderForm, ContactForm
from .models import *

# Create your views here.
@login_required(login_url='/user_auth/')
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')


@login_required(login_url='/user_auth/')
def tours(request):
    if request.user.is_authenticated:
        return render(request, 'tour_dates.html')


@login_required(login_url='/user_auth/')
def discography(request):
    """
    discography is a view function that renders the discography page.

    :param request: the request object

    :return: the discography page
    """
    data = Image.objects.all()
    albums = Album.objects.all()
    context = {'data': data, 'albums': albums}
    if request.user.is_authenticated:
        return render(request, 'discography.html', context)


def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            login(request, user)
            return redirect('/user_auth/')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index/')
            else:
                messages.error(request,"Invalid username or password.")
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

@login_required(login_url='/user_auth/')
def contact_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "General Inquiry"
                body = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'kb.masalesa@gmail.com', ['kb.masalesa@gmnail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('/contact/')

        form = ContactForm()
        return render(request, 'contact.html', {'contact_form': form})













