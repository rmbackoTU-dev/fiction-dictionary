from fict_dict.dataFile import dataFile
from fict_dict.fiction_dictionary import FictionDict
import unittest
import os
import sys
# TODO
'''
  Test implemented functions
  Implement worst case test
'''


class TestTempFile(unittest.TestCase):


    def setUp(self):
        self.currentdir=os.path.dirname(os.path.realpath(__file__))
        self.testFile=os.path.join(self.currentdir, 'testFileOne.json')
        self.testDict={"A": ["The quick brown fox jumps over the lazy dog"]}


    def tearDown(self):
        # Remove any temp files remaining after testing
        if os.path.isfile(self.testFile):
            os.remove(self.testFile)

    def test_BestCase(self):
        '''
        *creation
        *export
        *exportOverwrite
        *import
        *delete
        '''
        newDataFile=dataFile(os.getpid(), self.testFile )
        newFictDict=FictionDict('Test-Dictionary', self.testDict)
        newDataFile.exportJSON(newFictDict.getSerializableData())
        self.assertTrue(os.path.exists(newDataFile.file))
        #add a new word and export the dictionary to the same file
        newWord={"Bread" : ["A grainy food made from wheat and baked in an oven"]}
        newFictDict.addWord(newWord)
        newDataFile.exportOverwriteJSON(newFictDict.getSerializableData())
        #assert modifed, then test import and assert that the word was added
        inDict=newDataFile.importJSON()
        #test imported dict has same data as newFictDict
        self.assertEqual(inDict.data, newFictDict.data)
        self.assertEqual(inDict.name, newFictDict.name)
        #if the insert and import was sucessful we should find bread in the imported dictionary
        self.assertEqual(["Bread"], inDict.searchDict("Bread"))
        newDataFile.deleteJSON()
        self.assertFalse(os.path.exists(newDataFile.file))

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
        self.assertRaises(ValueError, dataFile, None, self.testFile)
        self.assertRaises(ValueError, dataFile, os.getpid(), '')
        newDataFile=dataFile(os.getpid(), self.testFile)
        self.assertRaises(ValueError, newDataFile.exportOverwriteJSON, None)
        ioErrorFile=os.path.join(self.currentdir, "fileNotAvailable.json")
        newDataFileTwo=dataFile(os.getpid(),  ioErrorFile)
        newDataFileThree=dataFile(os.getpid(), self.currentdir)
        self.assertRaises(IOError, newDataFileThree.exportJSON, self.testDict)
        self.assertRaises(IOError, newDataFileTwo.exportOverwriteJSON, self.testDict)
        self.assertRaises(IOError, newDataFileTwo.importJSON)
        self.assertRaises(IOError, newDataFileTwo.deleteJSON)
