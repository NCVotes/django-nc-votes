#!/usr/bin/env python3
"""
Models related to North Carolina voters and voting history.
"""
from .voter import Voter
from .voter_history import VoterHistory

__all__ = (
    'Voter',
    'VoterHistory',
)
