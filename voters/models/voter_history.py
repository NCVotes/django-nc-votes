#!/usr/bin/env python3
"""
Models related to voting history of North Carolina voters.
"""
from django.db import models
from .voter import Voter


class VoterHistory(models.Model):
    """
    The registration and voting status of a given voter in each election.
    """
    ncid = models.CharField('ncid', max_length=12, db_index=True)
    voter = models.ForeignKey(
        'Voter',
        on_delete=models.CASCADE,
        related_name="histories",
        to_field='ncid',
        null=True
    )
    county_id = models.SmallIntegerField('county_id', db_index=True)
    county_desc = models.CharField('county_desc', max_length=60, blank=True)
    voter_reg_num = models.CharField('voter_reg_num', max_length=12, blank=True)
    election_lbl = models.DateField( max_length=10, blank=True)
    election_desc = models.CharField('election_desc', max_length=230, blank=True, db_index=True)
    voting_method = models.CharField('voting_method', max_length=32, blank=True)
    voted_party_cd = models.CharField('voted_party_cd', max_length=3, blank=True)
    voted_party_desc = models.CharField('voted_party_desc', max_length=60, blank=True)
    pct_label = models.CharField('pct_label', max_length=6, blank=True)
    pct_description = models.CharField('pct_description', max_length=60, blank=True)
    voted_county_id = models.SmallIntegerField('voted_county_id')
    voted_county_desc = models.CharField('voted_county_desc', max_length=60, blank=True)
    vtd_label = models.CharField('vtd_label', max_length=6, blank=True)
    vtd_description = models.CharField('vtd_description', max_length=60, blank=True)

    class Meta:
        verbose_name = "Voter History"
        verbose_name_plural = "Voter Histories"
        db_table = 'voter_ncvhis'
