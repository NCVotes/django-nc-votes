#!/usr/bin/env python3
"""
Views for North Carolina voters 
"""
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Voter, VoterHistory


class VoterSampleView(LoginRequiredMixin, generic.ListView):
    """
    A sample of voters.
    """

    template_name = 'voters/sample.html'

    def get_queryset(self):
        """
        Return ten random voters.
        """
        return Voter.objects.order_by('?')[:10]


class VoterDetailView(LoginRequiredMixin, generic.DetailView):
    """
    A voter's full details.
    """

    model = Voter
    template_name = 'voters/detail.html'
