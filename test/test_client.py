import unittest
import sys
from unittest import mock
from fict_dict.client import CommandLineLib
#TODO:
#Test Interactive
#Test Help
#Test Create
#Test Select
#Test Remove
#Test Delete
#Test AddWord
#Test EditWord
#Test listDicts
#Test Save
#Test printWord
#Test printDict
#Test dictionaryAdd
#Test dictionaryCompare
#Test importJSON
#Implement and Test CommandLineMode
#Implement and test Search



#Replacement output redirection
class Output_redirect():

    def __init__(self):
        self.data=[]

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)

    def flush_output(self):
        del self.data[:]



class test_menu(unittest.TestCase):
    stdout_redirect=Output_redirect()
    #A new client
    testCLIClient=CommandLineLib()

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    #Add endlines to expected out
    def format_Expected(self, optDict):
        #Quick and easy dict value to list via comprehensions 
        expected_out=[i for  i  in optDict.values()]
        for i in range(len(expected_out)):
            current=expected_out[i]
            expected_out[i]=current+'\n'
        return expected_out


    def test_InteractiveLong(self, mock_print):
        self.fail('Test has not been implemented')
    
    def test_InteractiveShort(self, mock_print):
        self.fail('Test has not been implemented')

    def test_HelpShort(self):
        self.fail('Test has not been implemented')

    def test_HelpLong(self):
        self.fail('Test has not been implemented')

    def test_interactiveSysExit(self):
        self.fail('Test has not been implemented')

    def test_helpSysExit(self):
    	self.fail('Test has not been implemented')

    def test_Import(self):
    	self.fail('Test has not been implemented')

    def test_Create(self):
        self.fail('Test has not been implemented')

    def test_Select(self):
        self.fail('Test has not been implemented')

    def test_Remove(self):
        self.fail('Test has not been implemented')

    def test_Delete(self):
        self.fail('Test has not been implemented')

    def test_Edit(self):
    	self.fail('Test has not been implemented')

    def test_list(self):
    	self.fail('Test has not been implemented')

    def test_save(self):
        self.fail('Test has not been implemented')

    def test_printWord(self):
        self.fail('Test has not been implemented')

    def test_printDictionary(self):
        self.fail('Test has not been implemented')

    def test_dictionaryAdd(self):
    	self.fail('Test has not been implemented')

    def test_dictionaryCompare(self):
    	self.fail('Test has not been implemented')

    def test_Search(self):
    	self.fail('Test has not been implemented')