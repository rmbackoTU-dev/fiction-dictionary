import unittest
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.exceptions  import DuplicateWord
#TODO:
 # Fix current tests
# Add known failures to current tests
# Add words
# Edit Definitions
# Delete words
# Export Dictionaries to JSON
#  Import Dictionaries to JSON
#  Create word filter builder (Using Generators )
# Make unique definations with similar words Unique
#Connect to definition list
#Verify Uniqueness

class test_dictionary(unittest.TestCase):
    #make global empty test dictionaries
    testA=FictionDict()
    testC=FictionDict()

    def repopulateDict(self):
        '''
        Refreshes the test dictionaries after each test. Neccessary for test that add/ or subtract from base dictionary
        '''
        self.testA.name='TestA'
        self.testA.set_Data({'TAWord1' : ['aW1Def1'], 'TAWord2': ['aW2Def1']})
        self.testC.set_Data({'TCWord1' : ['cW1Def1', 'cW1Def2']})

    def setUp(self):
        self.repopulateDict()

    def tearDown(self):
        pass

    def test_add_dict(self):
    	'''
    	Add two dictionaries together test the results against a  known solution.
    	'''
    	compA=FictionDict('TestA', {"TAWord1" : ["aW1Def1"],  "TAWord2": ["aW2Def1"], 'TCWord1' : ['cW1Def1', 'cW1Def2']})
    	self.assertEqual(self.testA+self.testC, compA)

    def test_sub_dict(self):
    	'''
	    Subtract two dictionaries together test the results against a knwon solution. 
        Removes the word by the word key not by the definition
    	'''
    	sub_dict=FictionDict('TestA_Sub', {"TAWord1":  ["aW1Def1"]})
    	compS=FictionDict('TestA' , {'TAWord2' : ['aW2Def1'] })
    	self.assertEqual(self.testA-sub_dict, compS)

    def  test_repr_dict(self):
    	'''
            TestA should return
            FictionDict('TestA':{'TAWord1' : ['aW1Def1'],  'TAWord2': ['aW2Def1']})
        	 '''
    	compStr='FictionDict(TestA: {\'TAWord1\': [\'aW1Def1\'], \'TAWord2\': [\'aW2Def1\']})'
    	reprStr=repr(self.testA)
    	self.assertEqual(reprStr, compStr)
    
    def test_toString_dict(self):
    	'''
    	Test A should return
            "TAWord1:\t'aW1Def1'\nTAWord2:\taW2Def1\n"
    	'''
    	compStr="TAWord1:       \taW1Def1\nTAWord2:       \taW2Def1\n"
    	self.assertEqual(str(self.testA), compStr)

    def test_multi_toString_dict(self):
        '''
        Test should verify line returns after each definition
        '''
        compStr="TCWord1:       \tcW1Def1\ncW1Def2\n"
        self.assertEqual(str(self.testC), compStr)


    def test_word_add(self):
        '''
        Use word example to add to testA
        testA.addWord({'TAWord3' : 'aW3Def1'})
        should return
        testA.data.repr() ='FictionDict('Test', {"TAWord1" : ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1'] })''
        '''
        wordDictTest={'TAWord3' :  ['aW3Def1'] }
        testD=FictionDict('Test', {'TAWord1': ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1'] })
        self.testA.addWord(wordDictTest)
        self.assertEqual(self.testA.data, testD.data)

    def test_multi_word_add(self):
    	wordDictTest={'TAWord3' : ['aW3Def1'], 'TAWord4': ['aW4Def1']}
    	testD=FictionDict('Test', {'TAWord1': ['aW1Def1'], 'TAWord2': ['aW2Def1'],  'TAWord3' : ['aW3Def1'], 'TAWord4' : ['aW4Def1']})
    	self.testA.addWord(wordDictTest)
    	self.assertEqual(self.testA.data, testD.data)

    def test_multi_def_add(self):
        wordDictTest={'TAWord3' : ['aW3Def1', 'aW3Def2']}
        testD=FictionDict('Test', {"TAWord1" : ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1', 'aW3Def2'] })
        self.testA.addWord(wordDictTest)
        self.assertEqual(self.testA.data, testD.data)

    def test_multi_def_multi_word(self):
        wordDictTest={'TAWord3' : ['aW3Def1', 'aW3Def2'], 'TAWord4': ['aW4Def1']}
        testD=FictionDict('Test', {"TAWord1" : ['aW1Def1'], 'TAWord2' : ['aW2Def1'], 'TAWord3' : ['aW3Def1', 'aW3Def2'], 'TAWord4': ['aW4Def1'] })
        self.testA.addWord(wordDictTest)
        self.assertEqual(self.testA.data, testD.data)

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
        wordDictTest={"TAWord1": ['aW1Def1']}
        word=next(iter(wordDictTest))
        self.assertRaises(DuplicateWord, self.testA.isDuplicateWord, word)

    def test_KeyError_edit(self):
        editW='notInDict'
        editDef='blah'
        with self.assertRaises(KeyError ):
            self.testA.editWord(editW, editDef)

    def test_KeyError_delete(self):
        delW='notInDict'
        self.assertRaises(KeyError, self.testA.deleteWord, delW)

    def test_definition_edit_single(self):
        newDef='aW1Defn'
        testWord='TAWord1'
        testD=FictionDict('Test', {'TAWord1' : ['aW1Defn'], 'TAWord2': ['aW2Def1']})
        self.testA.editWord(testWord, newDef)
        self.assertEqual(self.testA.data, testD.data)

    def test_defintion_edit_multi(self):
        newDef='cW1Defn'
        testWord='TCWord1'
        testD=FictionDict('Test', {'TCWord1' : ['cW1Def1', 'cW1Defn']})
        self.testC.editWord(testWord, newDef, 1)
        self.assertEqual(self.testC.data, testD.data)

    def test_definition_add(self):
        newDef='cW1Def3'
        testWord='TCWord1'
        testD=FictionDict('Test', {'TCWord1' : ['cW1Def1', 'cW1Def2', 'cW1Def3']})
        self.testC.editWord(testWord, newDef, 2)
        self.assertEqual(self.testC.data, testD.data)

    def test_word_delete(self):
        delW='TAWord2'
        testD=FictionDict('Test', {'TAWord1' : ['aW1Def1']})
        self.testA.deleteWord(delW)
        self.assertEqual(self.testA.data, testD.data)

    def test_copyDict(self):
        testD=self.testA.copyDict()
        self.assertEqual(self.testA.data, testD.data)

    def test_importJSON(self):
        self.testA.exportJSON('TestA', '/home/ryan/dev/fiction_dictionary/dictionaries/')
        importJSON('TestD', '/home/ryan/dev/fiction_dictionary/dictionaries/TestA.json')
        self.assertEqual(self.testA.data, fDict.pop.data)

    def test_printWord(self):
        testWord='TCWord1'
        testStr=self.testC.wordToString(testWord)
        testWordLen=len(testWord)
        compStr="TCWord1:       \tcW1Def1\ncW1Def2\n"
        self.assertEqual(compStr, testStr)

    def test_buildFilter(self):
        self.fail("Not yet implemented --building a search Filter")

    def test_duplicateWord_typeErr_int(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, 1)

    def test_duplicateWord_typeErr_tuple(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, ('bar', 'baz') )

    def test_duplicateWord_typeErr_dict(self):
        self.assertRaises(TypeError, self.testA.isDuplicateWord, {1: 'bar'})

    def test_editWord_typeErr_intWord(self):
        defStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, 1, defStr)

    def test_editWord_typeErr_tupleWord(self):
        defStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, ('bar', 'baz'), defStr)

    def test_editWord_typeErr_dictWord(self):
        defStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, {1: 'bar'}, defStr)

    def test_editWord_typeErr_intDef(self):
        wrdStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrdStr, 1)

    def test_editWord_typeErr_tupleDef(self):
        wrdStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrdStr, ('bar', 'baz'))

    def test_editWord_typeErr_dictDef(self):
        wrdStr='foo'
        self.assertRaises(TypeError, self.testA.editWord, wrdStr, {1: 'bar'})

    def test_deleteWord_typeErr_int(self):
        self.assertRaises(TypeError, self.testA.deleteWord, 1)

    def test_deleteWord_typeErr_tuple(self):
        self.assertRaises(TypeError, self.testA.deleteWord, ('bar', 'baz'))

    def test_deleteWord_typeErr_dict(self):
        self.assertRaises(TypeError, self.testA.deleteWord, {1: 'bar'})

    def test_tempThreadTearDown(self):
        '''
        Test that after bash is closed  via exit from bash  thread is killed
        '''
        self.fail('Implement Thread tear down and signal functions')

    def test_tempFileAcess(self):
        '''
        Test that while temp process is open and has not recieved SIGINT from bash 
        that dictionary still has access to its temporary cache file
        '''
        self.fail('Implement temp file open fuctions. Call as part of tempt thread stand up')

    def test_tempTreadSetup(self):
        '''
        Test that when temp thread is up it can be called by main program
        '''
        self.fail('Implement temp file open fuctions. Call as part of tempt thread stand up')

    def test_tempFileTearDown(self):
        ''''
       Test that when thread is closed via exit from bash, that file is closed and is not accessible
        '''
        self.fail('Implement temp file open fuctions. Call as part of tempt thread stand up')



if __name__=='__main__':
    unittest.main()
