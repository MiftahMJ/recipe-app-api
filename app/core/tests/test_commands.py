"""
Test custom django masnagemeng=t"""

from unittest import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase



@patch('core.management.commands.wait_for_db.Command.check')
class CommanTest(SimpleTestCase):
    def test_wait_for_db_ready(self,patch_check):
        """test waiating for db if db ready"""
        patched_check.return_value = True
        call_command('wait_for_db')

        patch_check.assert_called_once_with(database=['default'])



    def test_wait_for_db_delay(self,patched_check):
        patched_check.side_effect = [Psycopg2Error] * 2 + \
           [OperationalError]* 3 + [True]