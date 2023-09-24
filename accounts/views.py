from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def cadastro_view(request):

    if request.POST and "username_cadastro" in request.POST:
        try:
            user = User.objects.get(username=request.POST['username_cadastro'])
        except:
            user = User.objects.create_user(
                request.POST["username_cadastro"],
                password=request.POST["password_cadastro"],
                email=request.POST["email_cadastro"],
            )
            auth.login(request, user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login_view(request):

    print("AQUI")

    if request.POST and "username_login" in request.POST:
        user = auth.authenticate(
            username= request.POST["username_login"],
            password=request.POST["password_login"],
        )
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout_view(request):

    if request.method == "POST":
        auth.logout(request)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))