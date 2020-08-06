from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.db import connection
import random
from django.contrib.auth.hashers import make_password
import math

def index(request):
    return render(request, 'attendance.html')
