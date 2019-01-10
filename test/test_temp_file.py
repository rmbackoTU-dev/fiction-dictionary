from fict_dict.dataTempFile import dataFile
import unittest
import os

#TODO
'''
  Test implemented functions
'''
class test_temp_file(unittest.TestCase):

    test_temp=dataFile()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def  test_createFile(self):
        try:
            result=self.test_temp.createFile()
            self.assertEqual(os.path.exists(self.test_temp.temp_abs), result)
        except:
            self.fail()

    def test_updateFile(self):
        self.fail()

    def test_deleteFile(self):
        self.fail()

    def test_printCurrent(self):
        self.fail()

    def  test_setContext(self):
        self.fail()

    def test_Contains(self):
        self.fail()
