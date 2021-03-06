from django.db import models

# Create your models here.
class NCVHis(models.Model):

    class Meta:
        verbose_name = "NC Voter History"
        verbose_name_plural = "NC Voter Histories"

    @staticmethod
    def parse_row(row):
        county_id = int(row['county_id'])
        row['county_id'] = county_id
        voted_county_id = int(row['voted_county_id'])
        row['voted_county_id'] = voted_county_id
        election_lbl_str = row['election_lbl']
        election_lbl_dt = datetime.strptime(election_lbl_str, '%m/%d/%Y')
        row['election_lbl'] = election_lbl_dt.date()
        return row

    @staticmethod
    def parse_existing(row):
        election_lbl_str = row.get('election_lbl')
        if election_lbl_str:
            election_lbl_dt = datetime.strptime(election_lbl_str, '%Y-%m-%d')
            row['election_lbl'] = election_lbl_dt.date()
        return row

    ncid = models.CharField('ncid', max_length=12, db_index=True)
    voter = models.ForeignKey('NCVoter', on_delete=models.CASCADE, related_name="histories", to_field='ncid', null=True)
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


class NCVoter(models.Model):

    class Meta:
        verbose_name = "NC Voter"
        verbose_name_plural = "NC Voters"

    @staticmethod
    def parse_row(row):
        county_id = int(row['county_id'])
        row['county_id'] = county_id
        birth_age = int(row['birth_age'])
        row['birth_age'] = birth_age
        drivers_lic_str = row.get('drivers_lic', '')
        drivers_lic = (drivers_lic_str == 'Y' or drivers_lic_str == 'y')
        row['drivers_lic'] = drivers_lic
        registr_dt_str = row['registr_dt']
        registr_dt = datetime.strptime(registr_dt_str, '%m/%d/%Y')
        row['registr_dt'] = registr_dt.date()
        confidential_ind_str = row.get('confidential_ind', '')
        row['confidential_ind'] = (confidential_ind_str == "Y")
        raw_birth_year = row.get('birth_year')
        if raw_birth_year:
            row['birth_year'] = int(raw_birth_year)
        return row

    @staticmethod
    def parse_existing(row):
        registr_dt_str = row.get('registr_dt')
        if registr_dt_str:
            registr_dt = datetime.strptime(registr_dt_str, '%Y-%m-%d')
            row['registr_dt'] = registr_dt.date()
        return row

    ncid = models.CharField('ncid', max_length=12, unique=True, db_index=True)
    county_id = models.SmallIntegerField(db_index=True)
    birth_age = models.IntegerField()
    birth_year = models.IntegerField(null=True)
    confidential_ind = models.BooleanField()
    birth_state = models.CharField('birth state', max_length=2)
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
    race_code = models.CharField('race_code', max_length=3)
    ethnic_code = models.CharField('ethnic_code', max_length=3)
    party_cd = models.CharField('party_cd', max_length=3)
    gender_code = models.CharField('gender_code', max_length=1)
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
