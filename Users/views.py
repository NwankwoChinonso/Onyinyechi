# Users/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import json
from django.contrib.auth import logout  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

User = get_user_model()

class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            
            if not username or not email or not password:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already in use"}, status=400)

            user = User.objects.create(username=username, email=email, password=make_password(password))
            return JsonResponse({"message": "User registered successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({"message": "User logged in successfully!"})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "User logged out successfully!"})

    
class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        return JsonResponse({
            "username": user.username,
            "email": user.email,
        })