from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeForm
# from user.forms import PasswordChange
from user.models import Profile
# from user.forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['user-first-name']
        last_name = request.POST['user-last-name']
        username = request.POST['user-name']
        password = request.POST['user-password']
        email = request.POST['user-email']

        if User.objects.filter(username=username).exists():
            messages.info(request, "User with this username already exists!")
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
            user.save()
            messages.success(request, f"Congratulations {username}! Your account has been created.")
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user-name']
        password = request.POST['user-password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Either username or password didn't match.")
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out of your account.")
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        profile = Profile(firstname=firstname, lastname=lastname, email=email, mobile=mobile)
        profile.save()
        messages.info(request, "Your details have been submitted.")
        return redirect('account')
    else:
        return render(request, 'my-account.html')

# def change_password(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your password was changed successfully.")
#             return redirect('home')
#         else:
#             form = PasswordChangeForm(user=request.user)
#         context = {'form':form}
#         return render(request, 'my-account.html', context)

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old-password')
        new_password1 = request.POST.get('new-password1')
        new_password2 = request.POST.get('new-password1')
        passw = PasswordChangeForm(old_password=old_password, new_password1=new_password1, new_password2=new_password2)
        passw.save()
        messages.info(request, "Your details have been submitted.")
        return redirect('account')
    else:
        return render(request, 'my-account.html')
