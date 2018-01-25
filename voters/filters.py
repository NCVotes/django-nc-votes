import django_filters
from .models import Voter


class VoterFilter(django_filters.FilterSet):
    birth_age__gt = django_filters.NumberFilter(
        name='birth_age',
        label='Age greater than',
        lookup_expr='gt',
    )
    birth_age__lt = django_filters.NumberFilter(
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
    race = django_filters.MultipleChoiceFilter(
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
    registr_dt__gt = django_filters.DateFilter(
        name='registr_dt',
        label='Registered after',
        lookup_expr='gt',
    )
    registr_dt__lt = django_filters.DateFilter(
        name='registr_dt',
        label='and before',
        lookup_expr='lt',
    )
    party_cd = django_filters.MultipleChoiceFilter(
        name='party_cd',
        label='Registered party',
        choices=Voter.PARTY_CHOICES,
    )

    class Meta:
        model = Voter
        exclude = [f.name for f in Voter._meta.get_fields()]
