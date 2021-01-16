from .serializers import UserSerializer, RegisterSerializer
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate

from .models import CreateUser
from .forms import CreateUserForm, LoginForm


# Create your views here.

def home(request):
    # if request.method == 'POST':
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        fm = CreateUserForm(request.POST or None)
        if fm.is_valid():
            fm.save()
            return render(request, 'login.html', {'form': fm})
    else:
        fm = CreateUserForm()

    return render(request, 'signup.html', {'form': fm})


def login(request):
    if request.method == 'POST':
        fm = LoginForm(request.POST)
        if fm.is_valid():
            fm.save()

        return render(request, 'login.html', {'form': fm})
    else:
        fm = LoginForm()
    return render(request, 'login.html', {'form': fm})


# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
