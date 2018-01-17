#!/usr/bin/env python3
"""voters app URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from .views import VoterSampleView, VoterDetailView

app_name = 'voters'
urlpatterns = [
    path('', VoterSampleView.as_view(), name='sample'),
    path('<int:pk>/', VoterDetailView.as_view(), name='detail'),
]