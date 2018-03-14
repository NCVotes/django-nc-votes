#!/usr/bin/env python3
"""
Models related to North Carolina electoral districts.
"""
from django.db import models
from django.contrib.postgres.functions import RandomUUID
from psycopg2 import sql
from .base import (
    VoterCharField,
    VoterSmallIntegerField,
)


class DistrictModelMixin(object):
    """
    """
    def get_composed_source_columns(self):
        """
        """
        return {
            'source_column_1': sql.Identifier(
                self._meta.fields[0].voter_column_name
            ),
            'source_column_2': sql.Identifier(
                self._meta.fields[1].voter_column_name
            )
        }

    def get_composed_target_columns(self):
        """
        """
        return {
            'target_column_1': sql.Identifier(self._meta.fields[0].name),
            'target_column_2': sql.Identifier(self._meta.fields[1].name),
        }


class County(models.Model, DistrictModelMixin):
    """
    A county in North Carolina.
    """
    voter_column_prefix = 'county'

    id = VoterSmallIntegerField(
        primary_key=True,
        help_text='Assigned by election authority.',
        voter_column_name='county_id',
    )
    description = VoterCharField(
        max_length=15,
        voter_column_name='county_desc',
    )

    class Meta:
        verbose_name_plural = "Counties"
        ordering = ['description']

    def __str__(self):
        return self.description        


# class Precinct(models.Model, DistrictModelMixin):
#     """
#     A precinct in North Carolina.
#     """
#     abbrv = VoterCharField(
#         max_length=6,
#         primary_key=True,
#         voter_column_name='precinct_abbrv',
#         help_text='Assigned by election authority.',
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='precinct_desc',
#     )


# class Municipality(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='municipality_abbrv',
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60
#     ),
#     voter_column_name='municipality_desc',


# class Ward(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='ward_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='ward_desc',
#     )


class CongressionalDistrict(models.Model, DistrictModelMixin):
    abbrv = VoterCharField(
        max_length=6,
        voter_column_name='cong_dist_abbrv',
        primary_key=True,
        help_text='Assigned by the election authority.'
    )
    description = VoterCharField(
        max_length=60,
        voter_column_name='cong_dist_abbrv',
    )

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


class SuperiorCourtDistrict(models.Model, DistrictModelMixin):
    abbrv = VoterCharField(
        max_length=6,
        voter_column_name='super_court_abbrv',
        primary_key=True,
        help_text='Assigned by the election authority.'
    )
    description = VoterCharField(
        max_length=60,
        voter_column_name='super_court_abbrv',
    )

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


# class JudicialDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='judic_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='judic_dist_abbrv',
#     )


class StateSenateDistrict(models.Model, DistrictModelMixin):
    abbrv = VoterCharField(
        max_length=6,
        voter_column_name='nc_senate_abbrv',
        primary_key=True,
        help_text='Assigned by the election authority.'
    )
    description = VoterCharField(
        max_length=60,
        voter_column_name='nc_senate_abbrv',
    )

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


class StateHouseDistrict(models.Model, DistrictModelMixin):
    abbrv = VoterCharField(
        max_length=6,
        voter_column_name='nc_house_abbrv',
        primary_key=True,
        help_text='Assigned by the election authority.'
    )
    description = VoterCharField(
        max_length=60,
        voter_column_name='nc_house_abbrv',
    )

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


# class CountyCommission(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='county_commiss_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='county_commiss_abbrv',
#     )


# class Township(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='township_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='township_desc',
#     )


# class SchoolDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='school_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='school_dist_desc',
#     )


# class FireDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='fire_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='fire_dist_desc',
#     )


# class WaterDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='water_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='water_dist_desc',
#     )


# class SewerDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='sewer_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='sewer_dist_desc',
#     )


# class SanitationDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='sanit_dist_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='sanit_dist_desc',
#     )


# class RescueDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='rescue_district_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='rescue_district_desc',
#     )


# class MunicDistrict(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='munic_district_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='munic_district_abbrv',
#     )


# class District1(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='dist_1_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='dist_1_desc',
#     )


# class District2(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='dist_2_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='dist_2_desc',
#     )


# class Vtd(models.Model, DistrictModelMixin):
#     abbrv = VoterCharField(
#         max_length=6,
#         voter_column_name='vtd_abbrv',
#         primary_key=True,
#         help_text='Assigned by the election authority.'
#     )
#     description = VoterCharField(
#         max_length=60,
#         voter_column_name='vtd_desc',
#     )
