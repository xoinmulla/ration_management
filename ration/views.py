from django.shortcuts import render
from .models import RationCard  # Ensure this model exists
from django.http import HttpResponse


def ration_cards(request):
    return render(request, 'ration/ration_cards.html')  # Ensure this template exists

def home(request):
    return render(request, 'ration/home.html') # Make sure 'home.html' exists in the right place

def members_view(request):
    return render(request, 'members/members.html')

def members_list(request):
    return render(request, 'members/members_list.html')  # ✅ Make sure this template exists!