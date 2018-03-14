#!/usr/bin/env python3
"""
Models related to North Carolina registered voters.
"""
from django.db import models
from .base import (
    VoterBooleanField,
    VoterCharField,
    VoterDateField,
    VoterForeignKey,
    VoterIntegerField,
)


class Voter(models.Model):
    """
    A person currently or previously registered to vote in North Carolina.
    """
    ncid = VoterCharField(
        'ncid',
        voter_column_name='ncid',
        primary_key=True,
        max_length=12, 
        db_index=True,
        help_text='Assigned by election authority.',
    )
    birth_age = VoterIntegerField(
        voter_column_name='birth_age',
    )
    birth_year = VoterIntegerField(
        voter_column_name='birth_year',
        null=True,
    )
    confidential_ind = VoterBooleanField(
        voter_column_name='confidential_ind',
        )
    STATE_CHOICES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
        ('AS', 'American Samoa'),
        ('GU', 'Guam'),
        ('MP', 'Northern Mariana Islands'),
        ('PR', 'Puerto Rico'),
        ('UM', 'U.S. Minor Outlying Islands'),
        ('VI', 'U.S. Virgin Islands'),
    )
    birth_state = VoterCharField(
        'birth state', 
        voter_column_name='birth_state',
        max_length=2,
        choices=STATE_CHOICES,
    )
    voter_reg_num = VoterCharField(
        voter_column_name='voter_reg_num',
        max_length=12,
    )
    status_cd = VoterCharField(
        voter_column_name='status_cd',
        max_length=2,
    )
    voter_status_desc = VoterCharField(
        voter_column_name='voter_status_desc',
        max_length=25,
    )
    reason_cd = VoterCharField(
        voter_column_name='reason_cd',
        max_length=2,
    )
    voter_status_reason_desc = VoterCharField(
        voter_column_name='voter_status_reason_desc',
        max_length=60,
    )
    name_prefx_cd = VoterCharField(
        voter_column_name='name_prefx_cd',
        max_length=4,
    )
    last_name = VoterCharField(
        voter_column_name='last_name',
        max_length=25,
    )
    middle_name = VoterCharField(
        voter_column_name='middle_name',
        max_length=25,
    )
    first_name = VoterCharField(
        voter_column_name='first_name',
        max_length=20,
    )
    name_suffix_lbl = VoterCharField(
        voter_column_name='name_suffix_lbl',
        max_length=30,
    )
    midl_name = VoterCharField(
        voter_column_name='midl_name',
        max_length=20,
    )
    name_sufx_cd = VoterCharField(
        voter_column_name='name_sufx_cd',
        max_length=3,
    )
    res_street_address = VoterCharField(
        voter_column_name='res_street_address',
        max_length=63,
    )
    res_city_desc = VoterCharField(
        voter_column_name='res_city_desc',
        max_length=60,
    )
    state_cd = VoterCharField(
        voter_column_name='state_cd',
        max_length=2,
    )
    zip_code = VoterCharField(
        voter_column_name='zip_code',
        max_length=9,
    )
    mail_addr1 = VoterCharField(
        voter_column_name='mail_addr1',
        max_length=40,
    )
    mail_addr2 = VoterCharField(
        voter_column_name='mail_addr2',
        max_length=40,
    )
    mail_addr3 = VoterCharField(
        voter_column_name='mail_addr3',
        max_length=40,
    )
    mail_addr4 = VoterCharField(
        voter_column_name='mail_addr4',
        max_length=40,
    )
    mail_city = VoterCharField(
        voter_column_name='mail_city',
        max_length=30,
    )
    mail_state = VoterCharField(
        voter_column_name='mail_state',
        max_length=2,
    )
    mail_zipcode = VoterCharField(
        voter_column_name='mail_zipcode',
        max_length=9,
    )
    full_phone_number = VoterCharField(
        voter_column_name='full_phone_number',
        max_length=12,
    )
    RACE_CHOICES = (
        ('B', 'African American/Black'),
        ('A', 'Asian'),
        ('I', 'American Indian/Alaska Native'),
        ('M', 'Multiracial'),
        ('O', 'Other'),
        ('U', 'Undesignated'),
        ('W', 'White'),
    )
    race_code = VoterCharField(
        voter_column_name='race_code',
        max_length=3,
        choices=RACE_CHOICES,
    )
    ETHNIC_CHOICES = (
        ('HL', 'Hispanic/Latino'),
        ('NL', 'Not Hispanic/Latino'),
        ('UN', 'Undesignated'),
    )
    ethnic_code = VoterCharField(
        voter_column_name='ethnic_code',
        max_length=3,
        choices=ETHNIC_CHOICES,
    )
    PARTY_CHOICES = (
        ('DEM', 'Democrat'),
        ('LIB', 'Libertarian'),
        ('REP', 'Republican'),
        ('UNA', 'Unaffiliated'),
    )
    party_cd = VoterCharField(
        voter_column_name='party_cd',
        max_length=3,
        choices=PARTY_CHOICES,
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undesignated'),
    )
    gender_code = VoterCharField(
        voter_column_name='gender_code',
        choices=GENDER_CHOICES,
        max_length=1,
    )
    birth_place = VoterCharField(
        voter_column_name='birth_place',
        max_length=30,
    )
    drivers_lic = VoterBooleanField(
        voter_column_name='drivers_lic',
    )
    registr_dt = VoterDateField(
        voter_column_name='registr_dt',
    )
    county = VoterForeignKey(
        'County',
        voter_column_name='county_id',
        on_delete=models.CASCADE,
        related_name="voters",
        help_text='Refers to the county in which the voter resides.',
    )
    congressional = VoterForeignKey(
        'CongressionalDistrict',
        voter_column_name='cong_dist_abbrv',
        db_column='congressional_district_abbrv',
        on_delete=models.CASCADE,
        related_name="voters",
        help_text='Refers to the congressional district in which the voter '
                  'resides.',
    )
    superior_court = VoterForeignKey(
        'SuperiorCourtDistrict',
        voter_column_name='super_court_abbrv',
        db_column='superior_court_district_abbrv',
        on_delete=models.CASCADE,
        related_name="voters",
        help_text='Refers to the superior court in which the voter resides.',
    )
    state_senate = VoterForeignKey(
        'StateSenateDistrict',
        voter_column_name='nc_senate_abbrv',
        db_column='state_senate_district_abbrv',
        on_delete=models.CASCADE,
        related_name="voters",
        help_text='Refers to the state senate district in which the voter '
                  'resides.',
    )
    state_house = VoterForeignKey(
        'StateHouseDistrict',
        voter_column_name='nc_house_abbrv',
        db_column='state_house_district_abbrv',
        on_delete=models.CASCADE,
        related_name="voters",
        help_text='Refers to the state house district in which the voter '
                  'resides.',
    )

    @property
    def full_name(self):
        """
        Voter's full name: last_name, suffix, first_name middle_name 
        """
        if self.name_suffix_lbl == '':
            full_name = f'{self.last_name}, {self.first_name} {self.middle_name}'.strip()
        else:
            full_name = f'{self.last_name}, {self.name_suffix_lbl}, {self.first_name} {self.middle_name}'.strip()

        return full_name

    def __str__(self):
        return f'{self.full_name} ({self.ncid})'
