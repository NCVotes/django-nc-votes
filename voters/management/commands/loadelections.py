#!/usr/bin/env python3
"""
Load Election model from distinct date/names in VoterHistory.
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.models import F
from django.db.utils import IntegrityError
from psycopg2 import sql
from voter.models import NCVHis
from voters.models import (
    Election, ElectionNameTranslator, VoterHistory
)
import re


class Command(BaseCommand):
    help = 'Load Election model from distinct date/names in VoterHistory'

    def handle(self, *args, **options):
        """
        Run full command routine.        
        """
        self.verbosity = options['verbosity']

        self.insert_translations()
        self.insert_elections()
        self.flush_voting_history()
        self.insert_voting_histories()

    def insert_translations(self):
        """
        Insert distinct election_lbl/election_desc combos into ElectionNameTranslator.
        """
        if self.verbosity > 1:
            self.stdout.write(
                f' Deleting old translations...'
            )

        ElectionNameTranslator.objects.all().delete()[0]

        sql_str = """
        INSERT INTO voters_electionnametranslator (date, raw_name, clean_name)
        SELECT 
            a.election_lbl as date,
            a.election_desc as raw_name,
            trim(
                substring(
                    a.election_desc from '^(?:(?:\d{1,2}\/|-){0,2}\d{2,5})?\s?(.+)$'
                )
            ) as clean_name
        FROM (
            SELECT DISTINCT election_lbl, election_desc
            FROM voter_ncvhis
        ) as a;
        """
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            if self.verbosity > 1:
                self.stdout.write(
                    f' Inserted {cursor.rowcount} translations...'
                )

        return

    def insert_elections(self):
        """
        Insert elections
        """
        date_name_combos = ElectionNameTranslator.objects.order_by(
            'date', 'clean_name'
        ).distinct(
            'date', 'clean_name',
        ).values(
            'date', 'clean_name',
        )
        for c in date_name_combos:
            try:
                new_election = Election.objects.create(
                    name=c['clean_name'], date=c['date']
                )
            except IntegrityError as e:
                if self.verbosity > 1:
                    self.stdout.write(
                        '  {clean_name} ({date}) already exists.'.format(**c)
                    )
            else:
                if self.verbosity > 1:
                    self.stdout.write(
                        f'  Created {new_election}.'
                    )

    def flush_voting_history(self):
        """
        Flush the Voter model.
        """
        if self.verbosity > 1:
            self.stdout.write(
                f' Flushing voter histories...'
            )
        
        count_deleted = VoterHistory.objects.all().delete()[0]
        
        if self.verbosity > 1:
            self.stdout.write(
                f'  {count_deleted} deleted.'
            )

        return

    def insert_voting_histories(self):
        """
        Insert voting histories.
        """
        if self.verbosity > 1:
            self.stdout.write(
                f' Reinserting voting histories...'
            )
        sql_str = """
        INSERT INTO voters_voterhistory (
            voter_id,
            voter_reg_num,
            election_id,
            voting_method,
            voted_party_cd,
            county_id,
            voted_county_id
        )
        SELECT 
            vh.ncid as voter_id,
            vh.voter_reg_num,
            e.id as election_id,
            vh.voting_method,
            vh.voted_party_cd,
            vh.county_id,
            vh.voted_county_id
        FROM voter_ncvhis vh
        JOIN voter_ncvoter v
        ON vh.voter_id = v.ncid
        JOIN voters_electionnametranslator t
        ON vh.election_lbl = t.date
        AND vh.election_desc = t.raw_name
        JOIN voters_election e
        ON t.date = e.date
        AND t.clean_name = e.name;
        """
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            if self.verbosity > 1:
                self.stdout.write(
                    f'Set election_id on {cursor.rowcount} rows.'
                )
        return
