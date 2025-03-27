from django.shortcuts import render
from .models import Member,RationCard  # Import the model

def ration_cards(request):
    return render(request, 'ration_cards.html')  # Ensure the template exists

def home(request):
    return render(request, 'home.html')  # Make sure 'home.html' exists in your templates folder

def ration_cards(request):
    members = Member.objects.all()  # Retrieve all members
    return render(request, 'members/ration_cards.html', {'members': members})

def members_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'members/members.html', {'members': members})

def ration_cards(request):
    ration_cards = RationCard.objects.all()  # Fetch all ration cards
    return render(request, 'members/ration_cards.html', {'ration_cards': ration_cards})


def members_view(request):
    return render(request, 'members/members.html')  # Ensure this path is correct

def members_list(request):
    members = Member.objects.all()  # Fetch all members
    return render(request, 'members/members_list.html', {'members': members})  # Pass members to template
