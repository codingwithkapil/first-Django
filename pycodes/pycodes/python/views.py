from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views import View
from django.urls import reverse


def index(request):
    return render(request, 'python1.html')