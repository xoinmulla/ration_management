from django.urls import path
from .views import ration_cards
from . import views
from members.views import members_view  # ✅ Correct way
from .views import members_list  # Make sure this is correctly imported


urlpatterns = [
    path('', views.home, name='home'),
    path('ration_cards/', views.ration_cards, name='ration_cards'),  # Must match views.py
    path('home/', members_view, name='members_page'), 
    path('members_list/', members_list, name='members_list'),  # ✅ Correct pattern
]
