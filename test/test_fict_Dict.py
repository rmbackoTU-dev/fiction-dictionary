import unittest
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.exceptions  import DuplicateWord
#TODO:
# Fix current tests
# Add Worst Case Test



class TestDictionary(unittest.TestCase):

    #make global empty test dictionaries
    testA = FictionDict()
    testC = FictionDict()

    '''
        Refreshes the test dictionaries after each test. Necessary for test that add/ or subtract from base dictionary
    '''
    def repopulateDict(self):
        self.testA.name = 'TestA'
        self.testA.set_Data({'TAWord1' : ['aW1Def1'], 'TAWord2': ['aW2Def1']})
        self.testC.set_Data({'TCWord1' : ['cW1Def1', 'cW1Def2']})

    def setUp(self):
        self.repopulateDict()

    def tearDown(self):
        pass

    '''
    Add two dictionaries together test the results against a  known solution.
    '''
    def test_add_dict(self):
        comp_a = FictionDict('TestA', {"TAWord1" : ["aW1Def1"],  "TAWord2": ["aW2Def1"], 'TCWord1' : ['cW1Def1', 'cW1Def2']})
        self.assertEqual(self.testA+self.testC, comp_a)

    '''
    Subtract two dictionaries together test the results against a knwon solution. 
    Removes the word by the word key not by the definition
    '''
    def test_sub_dict(self):
        sub_dict = FictionDict('TestA_Sub', {"TAWord1":  ["aW1Def1"]})
        comp_s = FictionDict('TestA' , {'TAWord2' : ['aW2Def1'] })
        self.assertEqual(self.testA-sub_dict, comp_s)

    '''
    TestA should return
    FictionDict('TestA':{'TAWord1' : ['aW1Def1'],  'TAWord2': ['aW2Def1']})
    '''
    def test_repr_dict(self):
        comp_str = 'FictionDict(TestA: {\'TAWord1\': [\'aW1Def1\'], \'TAWord2\': [\'aW2Def1\']})'
        repr_str = repr(self.testA)
        self.assertEqual(repr_str, comp_str)

    '''
    Test A should return
    "TAWord1:\t'aW1Def1'\nTAWord2:\taW2Def1\n"
    '''
    def test_toString_dict(self):
        comp_str = "TAWord1:       \taW1Def1\nTAWord2:       \taW2Def1\n"
        self.assertEqual(str(self.testA), comp_str)

    '''
    Test should verify line returns after each definition
    '''
    def test_multi_toString_dict(self):
        comp_str = "TCWord1:       \tcW1Def1\ncW1Def2\n"
        self.assertEqual(str(self.testC), comp_str)

    '''
    Use word example to add to testA
    testA.addWord({'TAWord3' : 'aW3Def1'})
    should return
    testA.data.repr() ='FictionDict('Test', {"TAWord1" : ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1'] })''
    '''
    def test_word_add(self):
        word_dict_test = {'TAWord3' :  ['aW3Def1']}
        self.testD = FictionDict('Test', {'TAWord1': ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1'] })
        self.testA.addWord(word_dict_test)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_multi_word_add(self):
        word_dict_test = {'TAWord3': ['aW3Def1'], 'TAWord4': ['aW4Def1']}
        self.testD = FictionDict('Test', {'TAWord1': ['aW1Def1'], 'TAWord2': ['aW2Def1'],  'TAWord3' : ['aW3Def1'], 'TAWord4' : ['aW4Def1']})
        self.testA.addWord(word_dict_test)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_multi_def_add(self):
        word_dict_test = {'TAWord3' : ['aW3Def1', 'aW3Def2']}
        self.testD = FictionDict('Test', {"TAWord1" : ['aW1Def1'], 'TAWord2': ['aW2Def1'], 'TAWord3' : ['aW3Def1', 'aW3Def2'] })
        self.testA.addWord(word_dict_test)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_multi_def_multi_word(self):
        word_dict_test={'TAWord3' : ['aW3Def1', 'aW3Def2'], 'TAWord4': ['aW4Def1']}
        self.testD=FictionDict('Test', {"TAWord1": ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3': ['aW3Def1', 'aW3Def2'], 'TAWord4': ['aW4Def1'] })
        self.testA.addWord(word_dict_test)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_set_type_err_str(self):
        print('Set data to String Test')
        self.assertRaises(TypeError, FictionDict.set_Data, 'Test String')

    def test_set_type_err_int(self):
        print('Set data to  Integer Test')
        self.assertRaises(TypeError, FictionDict.set_Data, 1)

    def test_set_type_err_tuple(self):
        print('Set  data to tuple test')
        self.assertRaises(TypeError, FictionDict.set_Data, ('A', {'test' : 'Just a test'}))

    def test_addWord_type_err_str(self):
        print('Add a string to data')
        self.assertRaises(TypeError, FictionDict.addWord, 'Test String')
    
    def test_addWord_type_err_int(self):
        print('Add a Integer to data')
        self.assertRaises(TypeError, FictionDict.addWord, 1)

    def test_addWord_type_err_tuple(self):
        print('Add a Tuple to data')
        self.assertRaises(TypeError, FictionDict.addWord, ('DefA', 'DefB'))

    def test_duplicateError(self):
        word_dict_test = {"TAWord1": ['aW1Def1']}
        word = next(iter(word_dict_test))
        self.assertRaises(DuplicateWord, self.testA.isDuplicateWord, word)

    def test_KeyError_edit(self):
        edit_word = 'notInDict'
        edit_defintion = 'blah'
        with self.assertRaises(KeyError ):
            self.testA.editWord(edit_word, edit_defintion)

    def test_KeyError_delete(self):
        del_word='notInDict'
        self.assertRaises(KeyError, self.testA.deleteWord, del_word)

    def test_definition_edit_single(self):
        new_def = 'aW1Defn'
        test_word = 'TAWord1'
        self.testD = FictionDict('Test', {'TAWord1': ['aW1Defn'], 'TAWord2': ['aW2Def1']})
        self.testA.editWord(test_word, new_def)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_defintion_edit_multi(self):
        new_def = 'cW1Defn'
        test_word = 'TCWord1'
        self.testD = FictionDict('Test', {'TCWord1': ['cW1Def1', 'cW1Defn']})
        self.testC.editWord(test_word, new_def, 1)
        self.assertEqual(self.testC.data, self.testD.data)

    def test_definition_add(self):
        new_def = 'cW1Def3'
        test_word = 'TCWord1'
        self.testD = FictionDict('Test', {'TCWord1': ['cW1Def1', 'cW1Def2', 'cW1Def3']})
        self.testC.editWord(test_word, new_def, 2)
        self.assertEqual(self.testC.data, self.testD.data)

    def test_word_delete(self):
        del_word = 'TAWord2'
        self.testD = FictionDict('Test', {'TAWord1': ['aW1Def1']})
        self.testA.deleteWord(del_word)
        self.assertEqual(self.testA.data, self.testD.data)

    def test_copyDict(self):
        self.testD = self.testA.copyDict()
        self.assertEqual(self.testA.data, self.testD.data)

    def test_printWord(self):
        test_word='TCWord1'
        test_str=self.testC.wordToString(test_word)
        test_word_len = len(test_word)
        comp_str="TCWord1:       \tcW1Def1\ncW1Def2\n"
        self.assertEqual(comp_str, test_str)
    '''
    '''
    def test_duplicateWord_typeErr_int(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, 1)

    def test_duplicateWord_typeErr_tuple(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, ('bar', 'baz'))

    def test_duplicateWord_typeErr_dict(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, {1: 'bar'})

    def test_editWord_typeErr_intWord(self):
        def_str = 'foo'
        self.assertRaises(TypeError, self.testA.editWord, 1, def_str)

    def test_editWord_typeErr_tupleWord(self):
        def_str = 'foo'
        self.assertRaises(TypeError, self.testA.editWord, ('bar', 'baz'), def_str)

    def test_editWord_typeErr_dictWord(self):
        def_str = 'foo'
        self.assertRaises(TypeError, self.testA.editWord, {1: 'bar'}, def_str)

    def test_editWord_typeErr_intDef(self):
        wrd_str='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrd_str, 1)

    def test_editWord_typeErr_tupleDef(self):
        wrd_str='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrd_str, ('bar', 'baz'))

    def test_editWord_typeErr_dictDef(self):
        wrd_str='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrd_str, {1: 'bar'})

    def test_deleteWord_typeErr_int(self):
        self.assertRaises(TypeError, self.testA.deleteWord, 1)

    def test_deleteWord_typeErr_tuple(self):
        self.assertRaises(TypeError, self.testA.deleteWord, ('bar', 'baz'))

    def test_deleteWord_typeErr_dict(self):
        self.assertRaises(TypeError, self.testA.deleteWord, {1: 'bar'})

    def test_search_word(self):
        self.fail("Test has not been implemented yet")

    def test_search_left_to_right(self):
        self.fail("Test has not been implemented yet")

    def test_search_right_to_left(self):
        self.fail("Test has not been implemented yet")

if __name__ == '__main__':
    unittest.main()
