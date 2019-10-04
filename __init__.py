from fict_dict.client import fict_dict_cli_access
from fict_dict.dataFile import dataFile
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.exceptions import DuplicateWord
from test.test_fict_Dict import TestDictionary
from test.TestDataFile import TestTempFile
from test.test_client import Test_client

__all__ = ['FictionDict', 'fict_dict_cli_access', 'DuplicateWord',  'dataFile', \
            'TestDictionary', 'TestTempFile', 'Test_client']
