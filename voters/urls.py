#!/usr/bin/env python3
"""voters app URL Configuration
"""
from django.contrib import admin
from django.urls import include, path, re_path
from .views import VoterSampleView, VoterDetailView, voter_count

app_name = 'voters'
urlpatterns = [
    path('', VoterSampleView.as_view(), name='sample'),
    re_path('(?P<ncid>[A-Z]{2}\d+)/', VoterDetailView.as_view(), name='detail'),
    path('count/', voter_count)
]