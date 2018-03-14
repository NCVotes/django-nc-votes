#!/usr/bin/env python3
"""
Models related to voting history of North Carolina voters.
"""
from django.db import models
from django.contrib.postgres.functions import RandomUUID
from .voter import Voter


class Election(models.Model):
    """
    An election in which a voter may have voted.
    """
    id = models.UUIDField(
        primary_key=True,
        default=RandomUUID(),
        editable=False,
        help_text='Randomly generated universal unique identifier.',
    )
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (("date", "name"),)
        ordering = ['-date', 'name']

    def __str__(self):
        return f'{self.name} ({self.date})'


class ElectionNameTranslator(models.Model):
    """
    """
    date = models.DateField()
    clean_name = models.CharField(max_length=100)
    raw_name = models.CharField(max_length=100)


class VoterHistory(models.Model):
    """
    The registration and voting status of a given voter in each election.
    """
    voter = models.ForeignKey(
        'Voter',
        on_delete=models.SET_NULL,
        related_name="histories",
        null=True,
    )
    voter_reg_num = models.CharField(max_length=12, blank=True)
    election = models.ForeignKey(
        'Election',
        on_delete=models.CASCADE,
        help_text='Refers to the election in which the vote was cast.'
    )
    voting_method = models.CharField(max_length=32, blank=True)
    voted_party_cd = models.CharField(max_length=3, blank=True)
    county_id = models.SmallIntegerField(db_index=True)
    voted_county_id = models.SmallIntegerField()
