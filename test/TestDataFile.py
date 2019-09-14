from fict_dict.dataFile import DataFile
import unittest
import os

# TODO
'''
  Test implemented functions
'''


class TestTempFile(unittest.TestCase):

    test_temp=DataFile()
    testDict={"A": ["The quick brown fox jumps over the lazy dog"]}
    testDictTwo={"Abba": ["A Band"], "Abba-Kadabra" : ["A magical command"]}

    def setUp(self):
        self.test_temp.setNewDictionary(self.testDict, "A")


    def tearDown(self):
        # Remove any temp files remaining after testing
        if os.path.isfile(self.test_temp.temp_abs):
            os.remove(self.test_temp.temp_abs)
        self.test_temp.set_new_dictionary({}, "")

    def test_set_new_dictionary(self):
        self.test_temp.set_new_dictionary(self.testDict, "testDict")
        self.assertEqual(self.test_temp.currentContext, self.testDict)

    def test_NoPID(self):
        pass

    def test_NoPathDir(self):
        pass

    def test_Export(self):
        pass

    def test_ExportOverwrite(self):
        pass

    def test_Import(self):
        pass

    def test_Delete(self):
        pass

    def test_DataFileExportIOError(self):
        pass

    def test_ExportOverWriteIOError(self):
        pass

    def test_InportIOError(self):
        pass

    def testDeleteIOError(self):
        pass