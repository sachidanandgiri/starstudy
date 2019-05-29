from django.shortcuts import render, redirect, reverse
from .models import Contact, User, UserProfileInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from study.forms import UserForm, UserProfileInfoForm
import smtplib
# Create your views here.


def index(request):
    return render(request, 'study/home.html')


def feature(request):
    return render(request, 'study/feature.html')


def price(request):
    return render(request, 'study/pricing.html')


def blog(request):
    return render(request, 'study/blog.html')


def blog_details(request):
    return render(request, 'study/blog_details.html')


def contact(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            obj = Contact(name=name, email=email, subject=subject, notes=message)
            obj.save()
            sender = 'sachinanandgiri@gmail.com'
            send_email(sender, '06august1991', email, subject, message)
            return render(request, 'study/contact.html')
        else:
            return render(request, 'study/contact.html')

    except Exception as e:
        print(e)


def send_email(user, password, recipient, subject, body):
    gmail_user = user
    gmail_pwd = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user_details = User.objects.get(username=username)
        user_info = UserProfileInfo.objects.get(user_id=user_details.id)
        if user:
            if user.is_active:
                request.session['username'] = username
                return render(request, 'study/student.html', {
                    'my_profile': user_details,
                    'user_info': user_info,
                })
            else:
                return HttpResponse('Your account was inactive!')
        else:
            print('Someone tried to login and failed!')
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse('Invalid Login details given!')
    else:
        try:
            if request.session['username'] != '':
                user_details = User.objects.get(username=request.session['username'])
                user_info = UserProfileInfo.objects.get(user_id=user_details.id)
                return render(request, 'study/student.html', {'my_profile': user_details, 'user_info': user_info,})
            else:
                return render(request, 'study/login.html')
        except Exception as e:
            print(e)
            return render(request, 'study/login.html')


def register(request):
    registered = False
    try:
        if request.method == "POST":
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
                    profile.user_type = '2'
                    if profile.save():
                        registered = True
                        HttpResponseRedirect(reverse('study:login'))
            else:

                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
    except Exception as e:
        print(e)
        # messages.add_message(request, messages.INFO, e)
    return render(request, 'study/registration.html', {'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'registered': registered,
                                                          })


def student(request):
    try:
        if request.session['username'] != '':
            return render(request, 'study/student.html')
        else:
            return render(request, 'study/login.html')
    except Exception as e:
        print(e)
        return render(request, 'study/login.html')


def user_logout(request):
    try:
        print(request.method)
        if request.method == "GET":
            return HttpResponseRedirect(reverse('study:login'))
        else:
            del request.session['username']
        return HttpResponseRedirect(reverse('study:login'))
    except Exception as e:
        print(e)