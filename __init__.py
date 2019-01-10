from fictdictCli import *
from fict_dict.fiction_dictionary import FictionDict 
from fict_dict.client import CommandLineLib
from fict_dict.exceptions import DuplicateWord
from fict_dict.dataTempFile import dataFile
from test.test_client import test_menu 
from test.test_fict_dict import test_dictionary
from test.test_temp_file import test_temp_file

__all__=['fict_dict.fiction_dictionary', 'fict_dict.client','fict_dict.exceptions',  'fict_dict.dataFile']
