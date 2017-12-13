#!/usr/bin/env python3
"""
Views for North Carolina voters 
"""
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Voter, VoterHistory


class VoterSampleView(generic.ListView):
    """
    A sample of voters.
    """
    template_name = 'voters/sample.html'

    def get_queryset(self):
        """
        Return ten random voters.
        """
        return Voter.objects.order_by('?')[:10]


class VoterDetailView(generic.DetailView):
    """
    A voter's full details.
    """
    model = Voter
    template_name = 'voters/detail.html'
