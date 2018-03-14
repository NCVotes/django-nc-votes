#!/usr/bin/env python3
"""
Load Election model from distinct date/names in VoterHistory.
"""
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from psycopg2 import sql
from voter.models import NCVoter


class Command(BaseCommand):
    help = 'Load voting districts.'

    def handle(self, *args, **options):
        """
        Run full command routine.        
        """
        self.verbosity = options['verbosity']
        for m in self.get_district_models():
            self.flush_district_model(m)
            self.load_district_model(m)

    def get_district_models(self):
        """
        Get the district models to load.
        """
        return [
            m for m in apps.get_app_config('voters').get_models()
            if 'districts' in m.__module__ and
            not m._meta.abstract
        ]

    def flush_district_model(self, model):
        """
        Flush a district model.
        """
        model_instance = model()

        if self.verbosity > 1:
            self.stdout.write(
                f' Flushing {model._meta.verbose_name_plural}...'
            )
        count_deleted = model.objects.all().delete()[0]
        if self.verbosity > 1:
            self.stdout.write(
                f'  {count_deleted} deleted.'
            )

        return

    def load_district_model(self, model):
        """
        Load a district model.
        """
        model_instance = model()

        sql_str = """
        INSERT INTO {target_table} ({target_column_1}, {target_column_2})
        SELECT DISTINCT {source_column_1}, {source_column_2}
        FROM {source_table};
        """
        composed_sql = sql.SQL(sql_str).format(
            target_table=sql.Identifier(model._meta.db_table),
            source_table=sql.Identifier(NCVoter._meta.db_table),
            **model_instance.get_composed_source_columns(),
            **model_instance.get_composed_target_columns(),
        )
        with connection.cursor() as cursor:
            cursor.execute(composed_sql)
            if self.verbosity > 1:
                self.stdout.write(
                    f'Inserted {cursor.rowcount} {model._meta.verbose_name_plural}.'
                )

        return
