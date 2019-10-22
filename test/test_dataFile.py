from fict_dict.dataFile import dataFile
import unittest
import os
import sys
# TODO
'''
  Test implemented functions
  Implement worst case test
'''


class TestTempFile(unittest.TestCase):
    currentdir=os.path.dirname(os.path.realpath(__file__))
    testFile=os.path.join(currentdir, 'testFileOne.json')
    testFileTwo=os.path.join(currentdir, 'testFileTwo.json')
    test_temp=dataFile(os.getpid(), currentdir)
    testDict={"A": ["The quick brown fox jumps over the lazy dog"]}
    testDictTwo={"Abba": ["A Band"], "Abba-Kadabra" : ["A magical command"]}

    def setUp(self):
        self.test_temp.setNewDictionary(self.testDict, "A")


    def tearDown(self):
        # Remove any temp files remaining after testing
        if os.path.isfile(self.test_temp.temp_abs):
            os.remove(self.test_temp.temp_abs)
        self.test_temp.set_new_dictionary({}, "")

    def test_BestCase(self):
        '''
        *creation
        *export
        *exportOverwrite
        *import
        *delete
        '''
        newDataFile=dataFile(os.getPid(), self.currentdir )
        self.fail("Test has not been implemented yet")

    def test_WorstCase(self):
        '''
        * no pid
        *no no path dir
        *test functions do not work without dictionary data
        *test export IOError
        *test export Overwrite file does not exist
        *test import IOError
        *test delete file does not exist
        '''
        self.fail("Test has not been implemented yet")