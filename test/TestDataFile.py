from fict_dict.dataFile import dataFile
import unittest
import os

# TODO
'''
  Test implemented functions
  Implement worst case test
'''


class TestTempFile(unittest.TestCase):

    test_temp=dataFile(os.getpid())
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
        self.fail("Test has not been implemented yet")

    def test_NoPathDir(self):
        self.fail("Test has not been implemented yet")

    def test_Export(self):
        self.fail("Test has not been implemented yet")

    def test_ExportOverwrite(self):
        self.test("Test has not been implemented yet")

    def test_Import(self):
        self.fail("Test has not been implemented yet")

    def test_Delete(self):
        self.fail("Test has not been implemented yet")

    def test_DataFileExportIOError(self):
        self.fail("Test has not been implemented yet")

    def test_ExportOverWriteIOError(self):
        self.fail("Test hase not been implemented yet")

    def test_ImportIOError(self):
        self.fail("Test has not been implemented yet")

    def testDeleteIOError(self):
        self.fail("Test has not been implemented yet")