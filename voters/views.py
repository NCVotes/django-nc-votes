#!/usr/bin/env python3
"""
Views for North Carolina voters 
"""
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import VoterFilter
from .models import Voter


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
    pk_url_kwarg = 'ncid'


@login_required
def voter_count(request):
    f = VoterFilter(request.GET)
    return render(
        request, 'voters/filter.html', {'filter': f, 'count': f.qs.count()}
    )
