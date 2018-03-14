#!/usr/bin/env python3
"""
Base classes for customizing Django's Model and ModelField subclasses.
"""
from django.db import models


class VoterFieldMixin(models.Field):
    """
    """
    def __init__(self, *args, voter_column_name=None, **kwargs):
        """
        Overrides the standard __init__ to add voter_column_name kwarg.
        """
        self.voter_column_name = voter_column_name
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Overrides the standard deconstruct method to add voter_column_name args.
        """
        name, path, args, kwargs = super().deconstruct()
        if self.voter_column_name:
            kwargs['voter_column_name'] = self.voter_column_name
        return name, path, args, kwargs


class VoterBooleanField(models.BooleanField, VoterFieldMixin):
    """
    """


class VoterCharField(models.CharField, VoterFieldMixin):
    """
    """


class VoterDateField(models.DateField, VoterFieldMixin):
    """
    """


class VoterForeignKey(models.ForeignKey, VoterFieldMixin):
    """
    """


class VoterIntegerField(models.IntegerField, VoterFieldMixin):
    """
    """


class VoterSmallIntegerField(models.SmallIntegerField, VoterFieldMixin):
    """
    """
