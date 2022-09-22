from django.contrib import auth
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.views import View
from .models import User
import logging

logging.basicConfig(filename="jinja_template.log", filemode="w")


class UserRegistrationView(View):

    def post(self, request):
        """
         Register user with given details
        :param request:
        :return:
        """
        try:
            User.objects.create_user(username=request.POST.get('username'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('first_name'),
                                            last_name=request.POST.get('last_name'),
                                            email=request.POST.get('email'),
                                            phone=request.POST.get('phone'))
            return redirect('login')
        except Exception as e:
            logging.exception(e)
            return render(request, 'registration.html')

    def get(self, request):
        return render(request, 'registration.html')


class LoginView(View):
    def post(self, request):
        """
        Checks whether username and password exist in our database and logs in
        :param request:
        :return:
        """
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
        except Exception as e:
            logging.exception(e)
            return render(request, 'login.html')

    def get(self, request):
        return render(request, 'login.html')


class PofileView(View):
    def get(self, request):
        return render(request, 'profile.html', context={'user': request.user})


