#!/usr/bin/env python3
"""
Models related to North Carolina registered voters.
"""
from django.db import models


class Voter(models.Model):
    """
    A person currently or previously registered to vote in North Carolina.
    """
    ncid = models.CharField('ncid', max_length=12, unique=True, db_index=True)
    county_id = models.SmallIntegerField(db_index=True)
    birth_age = models.IntegerField()
    birth_year = models.IntegerField(null=True)
    confidential_ind = models.BooleanField()
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
    birth_state = models.CharField(
        'birth state', max_length=2, choices=STATE_CHOICES,
    )
    age = models.TextField()
    county_desc = models.CharField('county_desc', max_length=15)
    voter_reg_num = models.CharField('voter_reg_num', max_length=12)
    status_cd = models.CharField('status_cd', max_length=2)
    voter_status_desc = models.CharField('voter_status_desc', max_length=25)
    reason_cd = models.CharField('reason_cd', max_length=2)
    voter_status_reason_desc = models.CharField('voter_status_reason_desc', max_length=60)
    # FIXME: Migrate to BooleanField
    absent_ind = models.CharField('absent_ind', max_length=1)
    name_prefx_cd = models.CharField('name_prefx_cd', max_length=4)
    last_name = models.CharField('last_name', max_length=25)
    middle_name = models.CharField('middle_name', max_length=25)
    first_name = models.CharField('first_name', max_length=20)
    name_suffix_lbl = models.CharField('name_suffix_lbl', max_length=30)
    midl_name = models.CharField('midl_name', max_length=20)
    name_sufx_cd = models.CharField('name_sufx_cd', max_length=3)
    res_street_address = models.CharField('res_street_address', max_length=63)
    res_city_desc = models.CharField('res_city_desc', max_length=60)
    state_cd = models.CharField('state_cd', max_length=2)
    zip_code = models.CharField('zip_code', max_length=9)
    mail_addr1 = models.CharField('mail_addr1', max_length=40)
    mail_addr2 = models.CharField('mail_addr2', max_length=40)
    mail_addr3 = models.CharField('mail_addr3', max_length=40)
    mail_addr4 = models.CharField('mail_addr4', max_length=40)
    mail_city = models.CharField('mail_city', max_length=30)
    mail_state = models.CharField('mail_state', max_length=2)
    mail_zipcode = models.CharField('mail_zipcode', max_length=9)
    full_phone_number = models.CharField('full_phone_number', max_length=12)
    RACE_CHOICES = (
        ('B', 'African American/Black'),
        ('A', 'Asian'),
        ('I', 'American Indian/Alaska Native'),
        ('M', 'Multiracial'),
        ('O', 'Other'),
        ('U', 'Undesignated'),
        ('W', 'White'),
    )
    race_code = models.CharField(
        'race_code', choices=RACE_CHOICES, max_length=3
    )
    ETHNIC_CHOICES = (
        ('HL', 'Hispanic/Latino'),
        ('NL', 'Not Hispanic/Latino'),
        ('UN', 'Undesignated'),
    )
    ethnic_code = models.CharField(
        'ethnic_code', choices=ETHNIC_CHOICES, max_length=3
    )
    PARTY_CHOICES = (
        ('DEM', 'Democrat'),
        ('LIB', 'Libertarian'),
        ('REP', 'Republican'),
        ('UNA', 'Unaffiliated'),
    )
    party_cd = models.CharField(
        'party_cd', choices=PARTY_CHOICES, max_length=3
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undesignated'),
    )
    gender_code = models.CharField('gender_code', max_length=1, choices=GENDER_CHOICES)
    birth_place = models.CharField('birth_place', max_length=30)
    drivers_lic = models.BooleanField('drivers_lic')
    registr_dt = models.DateField('registr_dt')
    precinct_abbrv = models.CharField('precinct_abbrv', max_length=6)
    precinct_desc = models.CharField('precinct_desc', max_length=60)
    municipality_abbrv = models.CharField('municipality_abbrv', max_length=6)
    municipality_desc = models.CharField('municipality_desc', max_length=60)
    ward_abbrv = models.CharField('ward_abbrv', max_length=6)
    ward_desc = models.CharField('ward_desc', max_length=60)
    cong_dist_abbrv = models.CharField('cong_dist_abbrv', max_length=6)
    super_court_abbrv = models.CharField('super_court_abbrv', max_length=6)
    judic_dist_abbrv = models.CharField('judic_dist_abbrv', max_length=6)
    nc_senate_abbrv = models.CharField('nc_senate_abbrv', max_length=6)
    nc_house_abbrv = models.CharField('nc_house_abbrv', max_length=6)
    county_commiss_abbrv = models.CharField('county_commiss_abbrv', max_length=6)
    county_commiss_desc = models.CharField('county_commiss_desc', max_length=60)
    township_abbrv = models.CharField('township_abbrv', max_length=6)
    township_desc = models.CharField('township_desc', max_length=60)
    school_dist_abbrv = models.CharField('school_dist_abbrv', max_length=6)
    school_dist_desc = models.CharField('school_dist_desc', max_length=60)
    fire_dist_abbrv = models.CharField('fire_dist_abbrv', max_length=6)
    fire_dist_desc = models.CharField('fire_dist_desc', max_length=60)
    water_dist_abbrv = models.CharField('water_dist_abbrv', max_length=6)
    water_dist_desc = models.CharField('water_dist_desc', max_length=60)
    sewer_dist_abbrv = models.CharField('sewer_dist_abbrv', max_length=6)
    sewer_dist_desc = models.CharField('sewer_dist_desc', max_length=60)
    sanit_dist_abbrv = models.CharField('sanit_dist_abbrv', max_length=6)
    sanit_dist_desc = models.CharField('sanit_dist_desc', max_length=60)
    rescue_dist_abbrv = models.CharField('rescue_dist_abbrv', max_length=6)
    rescue_dist_desc = models.CharField('rescue_dist_desc', max_length=60)
    munic_dist_abbrv = models.CharField('munic_dist_abbrv', max_length=6)
    munic_dist_desc = models.CharField('munic_dist_desc', max_length=60)
    dist_1_abbrv = models.CharField('dist_1_abbrv', max_length=6)
    dist_1_desc = models.CharField('dist_1_desc', max_length=60)
    dist_2_abbrv = models.CharField('dist_2_abbrv', max_length=6)
    dist_2_desc = models.CharField('dist_2_desc', max_length=60)
    vtd_abbrv = models.CharField('vtd_abbrv', max_length=6)
    vtd_desc = models.CharField('vtd_desc', max_length=60)

    class Meta:
        db_table = 'voter_ncvoter'
