from django.contrib.auth import login, get_user_model, logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()


def signup(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)

        login(request, user)

        return redirect('index')

    return render(request, 'accounts/signup.html')


# login_user
def login_user(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html')


# logout_user
def logout_user(request):
    logout(request)

    return redirect('index')
