import unittest
from fict_dict.fiction_dictionary import FictionDict
import collections
#TODO:
# Fix current tests
# Add Worst Case Test
# Fix issues with exceptions


class TestDictionary(unittest.TestCase):

    #make global empty test dictionaries
    testA = FictionDict()
    testC = FictionDict()

    '''
        Refreshes the test dictionaries after each test. Necessary for test that add/ or subtract from base dictionary
    '''
    def repopulateDict(self):
        self.testA.name = 'TestA'
        self.testC.name = 'TestC'
        self.testA.set_Data({'TAWord1' : ['aW1Def1'], 'TAWord2': ['aW2Def1']})
        self.testC.set_Data({'TCWord1' : ['cW1Def1', 'cW1Def2']})

    def setUp(self):
        self.repopulateDict()

    def tearDown(self):
        pass
        #self.repopulateDict()

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
        comp_str = "TAWord1:\taW1Def1\nTAWord2:\taW2Def1\n"
        self.assertEqual(str(self.testA), comp_str)

    '''
    Test should verify line returns after each definition
    '''
    def test_multi_toString_dict(self):
        comp_str = "TCWord1:\tcW1Def1\n\tcW1Def2\n"
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
        self.assertEqual(self.testA.isDuplicateWord(word), True)

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
        print(self.testC.__str__())
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
        comp_str="TCWord1:\tcW1Def1\n\tcW1Def2\n"
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

    '''
    Search Test will use the W section of the dictionary featured
    in 'Dune' by  Frank Herbert, and the sub strings of
    'Wa', 'taw', 'en', and 'Water'
    @input
    'Water Burden'
    'Water Counter
    'Water Discipline'
    'Waterman'
    'Water Tube'
    'Way, Bene Gesserit'
    'Weather Scanner'
    'Weirding'
    'Wind trap'
    
    @expected outputs
    For Wa
    wa_expected=['Water Burden', /
    'Water Counter', /
    'Water Discipline', /
    'Waterman', /
    'Water Tube', /
    'Way, Bene Gesserit']
    
    For 'taw'
    taw_expected=['Water Burden', \ 
    'Water Counter', \
    'Water Discipline', \
    'Waterman', \
    'Water Tube' ]
    
    For en:
    en_expected=['Water Burden', \
    'Water Discipline', \
    'Way Bene Gesserit', \
    'Water Scanner']
    
    For water:
    water_expected=['Water Burden', /
    'Water Counter', /
    'Water Discipline', /
    'Waterman', /
    'Water Tube']
    '''
    def test_search_word(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water Tube' : ['defFill5'], \
                'Water of Life' : ['defFill6'], \
                'Way, Bene Gesserit': ['defFill7'], \
                'Weather Scanner': ['defFill8'], \
                'Weirding': ['defFill9'], \
                'Wind Trap': ['defFill10'] }
        w_dict.addWord(w_dict_data)
        wa_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life', \
    '   Way, Bene Gesserit']
        wat_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life']
        en_expected=['Water Burden', \
        'Water Discipline', \
        'Way Bene Gesserit', \
        'Water Scanner']
        water_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life']
        wa_actual=w_dict.searchDict('Wa')
        wat_actual=w_dict.searchDict('Wat')
        en_actual=w_dict.searchDict('en')
        water_actual=w_dict.searchDict('Water')
        self.assertTrue(self.compareList(wa_expected, wa_actual), \
                        "'Wa' list do no match")
        self.assertTrue(self.compareList(wat_expected, water_actual), \
                        "'Wat' list do not match")
        self.assertTrue(self.compareList(en_expected, en_actual), \
                        "'en' list do not match")
        self.assertTrue(self.compareList(water_expected, water_actual), \
                        "'Water' list do not match")

    def test_search_left_to_right(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water Tube' : ['defFill5'], \
                'Water of Life' : ['defFill6'], \
                'Way, Bene Gesserit': ['defFill7'], \
                'Weather Scanner': ['defFill8'], \
                'Weirding': ['defFill9'], \
                'Wind Trap': ['defFill10'] }
        w_dict.addWord(w_dict_data)
        wa_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life', \
    '   Way, Bene Gesserit']
        en_expected=['Water Burden','Way Bene Gesserit']
        water_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life']
        wa_actual=w_dict.left_to_right_match_list('Wa')
        en_actual=w_dict.left_to_right_match_list('en')
        water_actual=w_dict.left_to_right_match_list('Water')
        self.assertTrue(self.compareList(wa_expected, wa_actual), \
                        "'Wa' List are not equal")
        self.assertTrue(self.compareList(en_expected, en_actual), \
                        "'en' List are not equal")
        self.assertTrue(self.compareList(water_expected, water_actual), \
                        "'water' list are not equal")


    def test_search_right_to_left(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water Tube' : ['defFill5'], \
                'Water of Life' : ['defFill6'], \
                'Way, Bene Gesserit': ['defFill7'], \
                'Weather Scanner': ['defFill8'], \
                'Weirding': ['defFill9'], \
                'Wind Trap': ['defFill10'] }
        w_dict.addWord(w_dict_data)
        wat_expected=['Water Burden', \
        'Water Counter', \
        'Water Discipline', \
        'Waterman', \
        'Water Tube', \
        'Water of Life']
        en_expected=['Water Burden', \
        'Water Discipline', \
        'Way Bene Gesserit', \
        'Water Scanner']
        wat_actual=w_dict.right_to_left_match_list('Wat')
        en_actual=w_dict.right_to_left_match_list('en')
        self.assertTrue(self.compareList(wat_expected, wat_actual), \
                        "'Wat' list are not equal")
        self.assertTrue(self.compareList(en_expected, en_actual), \
                        "'en' list are not equal")
    '''
    Test exeptions are properly thrown by search 
    '''
    def test_search_word_WorstCase(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water of Life': ['defFill5'], \
                'Way, Bene Gesserit': ['defFill6'], \
                'Weather Scanner': ['defFill7'], \
                'Weirding': ['defFill8'], \
                'Wind Trap': ['defFill9'] }
        w_dict.addWord(w_dict_data)
        emptySearchWord=''
        nonStringSearchWord=['A Word']
        self.assertRaises(ValueError, w_dict.searchDict, emptySearchWord)
        self.assertRaises(TypeError, w_dict.searchDict, nonStringSearchWord)

    '''
    Test exceptions are properly thrown by left to right search
    '''
    def test_search_left_to_right_WorstCase(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water of Life': ['defFill5'], \
                'Way, Bene Gesserit': ['defFill6'], \
                'Weather Scanner': ['defFill7'], \
                'Weirding': ['defFill8'], \
                'Wind Trap': ['defFill9'] }
        w_dict.addWord(w_dict_data)
        emptySearchWord=''
        nonStringSearchWord=['A Word']
        self.assertRaises(ValueError, w_dict.left_to_right_match_list, emptySearchWord)
        self.assertRaises(TypeError, w_dict.left_to_right_match_list, nonStringSearchWord)

    '''
    Test exceptions are properly thrown by right to left search
    '''
    def test_search_right_to_left_WorstCase(self):
        w_dict=FictionDict()
        w_dict_data={'Water Burden': ['defFill1'], \
                'Water Counter': ['defFill2'], \
                'Water Discipline': ['defFill3'] , \
                'Waterman': ['defFill4'], \
                'Water of Life': ['defFill5'], \
                'Way, Bene Gesserit': ['defFill6'], \
                'Weather Scanner': ['defFill7'], \
                'Weirding': ['defFill8'], \
                'Wind Trap': ['defFill9'] }
        w_dict.addWord(w_dict_data)
        emptySearchWord=''
        nonStringSearchWord=['A Word']
        self.assertRaises(ValueError, w_dict.right_to_left_match_list, emptySearchWord)
        self.assertRaises(TypeError, w_dict.right_to_left_match_list, nonStringSearchWord)

    def compareList(self, listOne, listTwo):
        counterOne=collections.Counter(listOne)
        counterTwo=collections.Counter(listTwo)
        wordsFound=0
        for k, v in counterOne.items():
            current_count=v
            listTwoKey=list(counterTwo.keys())
            listTwoSize=len(listTwoKey)
            i=0
            l=""
            cmp_count=0
            while((i < listTwoSize) and l != k):
                l=listTwoKey[i]
                i=i+1
                cmp_count=counterTwo[l]
            if (current_count == cmp_count):
                wordsFound=wordsFound+1

        match=(wordsFound == listTwoSize)
        return match



if __name__ == '__main__':
    unittest.main()
