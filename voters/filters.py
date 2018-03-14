import django_filters
from .models import (
    Voter,
    Election,
    County,
    CongressionalDistrict,
    StateSenateDistrict,
    StateHouseDistrict,
    SuperiorCourtDistrict,
)


class VoterFilter(django_filters.FilterSet):
    birth_age_gt = django_filters.NumberFilter(
        name='birth_age',
        label='Age greater than',
        lookup_expr='gt',
    )
    birth_age_lt = django_filters.NumberFilter(
        name='birth_age',
        label='and less than',
        lookup_expr='lt',
    )
    birth_state = django_filters.MultipleChoiceFilter(
        name='birth_state',
        label='Birth state',
        choices=Voter.STATE_CHOICES,
    )
    gender_code = django_filters.MultipleChoiceFilter(
        name='gender_code',
        label='Gender',
        choices=Voter.GENDER_CHOICES,
    )
    race_code = django_filters.MultipleChoiceFilter(
        name='race_code',
        label='Race',
        choices=Voter.RACE_CHOICES,
        null_label='(blank)'
    )
    ethnic_code = django_filters.ChoiceFilter(
        name='ethnic_code',
        label = 'Ethnicity',
        choices=Voter.ETHNIC_CHOICES,
    )
    registr_dt_gt = django_filters.DateFilter(
        name='registr_dt',
        label='Registered after',
        lookup_expr='gt',
    )
    registr_dt_lt = django_filters.DateFilter(
        name='registr_dt',
        label='and before',
        lookup_expr='lt',
    )
    party_cd = django_filters.MultipleChoiceFilter(
        name='party_cd',
        label='Registered party',
        choices=Voter.PARTY_CHOICES,
    )
    county = django_filters.ModelMultipleChoiceFilter(
        name='county',
        label='County',
        queryset=County.objects.all(),
    )
    congressional = django_filters.ModelMultipleChoiceFilter(
        name='congressional',
        label='Congressional District',
        queryset=CongressionalDistrict.objects.exclude(abbrv=''),
    )
    state_senate = django_filters.ModelMultipleChoiceFilter(
        name='state_senate',
        label='State Senate District',
        queryset=StateSenateDistrict.objects.exclude(abbrv=''),
    )
    state_house = django_filters.ModelMultipleChoiceFilter(
        name='state_house',
        label='State House District',
        queryset=StateHouseDistrict.objects.exclude(abbrv=''),
    )
    superior_court = django_filters.ModelMultipleChoiceFilter(
        name='superior_court',
        label='Superior Court District',
        queryset=SuperiorCourtDistrict.objects.exclude(abbrv=''),
    )
    histories_election_include = django_filters.ModelMultipleChoiceFilter(
        name='histories__election',
        label='Voted in',
        queryset=Election.objects.all(),
    )
    histories_election_exclude = django_filters.ModelMultipleChoiceFilter(
        name='histories__election',
        label='Did not vote in',
        queryset=Election.objects.all(),
        exclude=True,
    )

    class Meta:
        model = Voter
        exclude = [f.name for f in Voter._meta.get_fields()]
