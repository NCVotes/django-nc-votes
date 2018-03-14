#!/usr/bin/env python3
"""
Load Voter model from NCVoter.
"""
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.models import F
from django.db.utils import IntegrityError
from psycopg2 import sql
from voters.models import Voter
from voter.models import NCVoter


class Command(BaseCommand):
    help = 'Load Voter model from NCVoter'

    def handle(self, *args, **options):
        """
        Run full command routine.        
        """
        self.verbosity = options['verbosity']
        self.source_table = apps.get_app_config('voter').get_model('NCVoter')
        self.target_table = apps.get_app_config('voters').get_model('Voter')
        
        self.flush_voters()
        self.load_voters()

    def flush_voters(self):
        """
        Flush the Voter model.
        """
        if self.verbosity > 1:
            self.stdout.write(
                f' Flushing voters...'
            )
        
        count_deleted = self.target_table.objects.all().delete()[0]
        
        if self.verbosity > 1:
            self.stdout.write(
                f'  {count_deleted} deleted.'
            )

        return

    def get_target_columns(self):
        """
        Return a list of target database columns.
        """
        return [
            f for f in self.target_table._meta.get_fields()
            if f.concrete
        ]

    def get_composable_target_columns(self):
        """
        Return a list of target database columns as a sequence of Composables.
        """
        return [
            sql.Identifier(f.column) for f in self.get_target_columns()
        ]

    def get_composable_source_columns(self):
        """
        Return a list of source database columns as a sequence of Composables.
        """
        return [
            sql.Identifier(f.voter_column_name) for f in self.get_target_columns()
        ]

    def load_voters(self):
        """
        Load the Voter model.
        """
        sql_str = """
        INSERT INTO {target_table} ({target_columns})
        SELECT {source_columns}
        FROM {source_table};
        """

        composed_sql = sql.SQL(sql_str).format(
            target_table=sql.Identifier(Voter._meta.db_table),
            source_table=sql.Identifier(NCVoter._meta.db_table),
            target_columns=sql.SQL(', ').join(
                self.get_composable_target_columns()
            ),
            source_columns=sql.SQL(', ').join(
                self.get_composable_source_columns()
            ),
        )

        with connection.cursor() as cursor:
            cursor.execute(composed_sql)
            if self.verbosity > 1:
                self.stdout.write(
                    f'Inserted {cursor.rowcount} voters.'
                )
        return
