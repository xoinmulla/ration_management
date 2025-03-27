from django.urls import path
from .views import ration_cards
from .views import members_view  # Import the vie
from . import views
from .views import members_list  # Make sure this is correctly imported

urlpatterns = [
     path('', views.home, name='members'),  # Make sure 'views.home' exists
     path('ration_cards/', views.ration_cards, name='ration_cards'),  # Must match views.py
     path('', members_view, name='members_page'),   # Home page for members
     path('ration_cards/', views.ration_cards, name='ration_cards'),
       path('members_list/', members_list, name='members_list'),  # ✅ Correct pattern
    

]
