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
        pass

    def tearDown(self):
        # Remove any temp files remaining after testing
        if os.path.isfile(self.test_temp.temp_abs):
            os.remove(self.test_temp.temp_abs)
        self.test_temp.set_new_dictionary({}, "")

    def test_set_new_dictionary(self):
        self.test_temp.set_new_dictionary(self.testDict, "testDict")
        self.assertEqual(self.test_temp.currentContext, self.testDict)

    def test_create_file(self):
        try:
            result_dict = self.createFile_Helper()
            self.assertTrue(os.path.isfile(self.test_temp.temp_abs))
        except IOError:
            self.fail("An unexpected FileError occured")

    def test_create_file_with_file(self):
        try:
            result_dict=self.createFile_Helper()
            self.assertEqual(result_dict["currentContext"], self.testDict)
        except IOError:
            self.fail("An unexpected FileError occured")

    def test_createFile_error_message(self):
        try:
            result_dict=self.test_temp.create_file()
            expected_error_msg="No default dictionary context was set create a populated dictionary first"
            self.assertEqual(result_dict["Error0"], expected_error_msg)
        except IOError:
            self.fail("An unexpected FileError occured")

    def test_updateFile(self):
        self.fail()

    def test_deleteFile(self):
        self.fail()

    def test_printCurrentSingle(self):
        self.fail()

    def test_printCurrentMultiple(self):
        self.fail()

    def  test_setContext(self):
        self.fail()

    def test_Contains(self):
        self.fail()

    def createFile_Helper(self):
        self.test_temp.set_new_dictionary(self.testDict, "testDict")
        result = self.test_temp.create_file()
        return result
