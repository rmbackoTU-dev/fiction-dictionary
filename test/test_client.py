import unittest
from fict_dict.client import fict_dict_cli_access

#TODO:
#Test create
#Test Delete
#Test Edit
#Test Copy
#Test Dictionary Add
#Test Dictionary Compare
#Test Get word String
#Test Get Dict String
#Test Search for word
#Test Search for def
#Test Left to right word search
#Test Right to left word search
#Test Left to right dictionary search
#Test Right to left dictionary Search


class Test_client(unittest.TestCase):
    #A new client
    testClientInterface=fict_dict_cli_access()

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_Create_Dictionary(self):
        self.fail('Test has not been implemented')

    def test_Create_Dictionary_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_Delete_Dictionary(self):
        self.fail('Test has not been implemented')

    def test_Delete_Dictionary_WorstCase(self):
         self.fail('Test has not been implemented')

    def test_Edit_Dictionary(self):
        self.fail('Test has not been implemented')

    def test_Edit_Dictionary_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_Copy_Dictionary_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_dictionary_Add(self):
        self.fail('Test has not been implemented')

    def test_dictionary_Add_WorstCase(self):
        self.fail("Test has not been implemented")

    def test_dictionaryCompare(self):
        self.fail('Test has not been implemented')

    def test_dictionary_Compare_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_get__word_from_Dict(self):
       self.fail('Test has not been implemented')

    def test_get_word_from_Dict_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_get_dictionary_string(self):
        self.fail('Test has not been implemented')

    def test_get_dictionary_string_wWrstCase(self):
        self.fail('Test has not been implemented')

    def test_Search_Dictionary(self):
        self.fail('Test has not been implemented')

    def test_Search_Dictionary_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_Search_Dictionary_FromLeft(self):
        self.fail('Test has not been implemented')

    def test_Search_Dictionary_FromLeft_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_FromRight(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_FromRight_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_ret_Def(self):
        self.fail('Test has not been implemented')

    def test_search_Dictiaonary_ret_Def_WorseCase(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_ret_Def_FromLeft(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_ret_Def_FromLeft_WorstCase(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_ret_Def_FromRight(self):
        self.fail('Test has not been implemented')

    def test_search_Dictionary_ret_Def_FromRight_WorstCase(self):
        self.fail('Test has not been implemented')
