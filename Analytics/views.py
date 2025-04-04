from django.shortcuts import render
from .models import UserVisit
from django.http import JsonResponse

def get_user_visits(request):
    visits = UserVisit.objects.all()
    visits_data = [{"user": visit.user.username, "time": visit.visit_time, "page": visit.page_visited} for visit in visits]
    return JsonResponse(visits_data, safe=False)