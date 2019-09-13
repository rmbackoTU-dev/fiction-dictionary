import json, sys, os
from collections import UserDict, defaultdict
from fict_dict.exceptions import DuplicateWord
import time

#TODO
 #Fix the formating on str
 #Fix add the dictionary name to the JSON file
 #Implement Word Filter
class FictionDict(UserDict):
    '''
    Fiction Dictionary Class: inherits from UserDict dict wrapper
    Description: used to create fiction dictionaries which can be saved to exported from json files
    todo:
    Redefine key error continue to clean up error handling
    '''

    #Keep class generation generic do the fancy stuff later
    def __init__(self, name="",  data=dict(), **kwargs):
        UserDict.__init__(self)
        self.name=name
        self.update(data)
        self.update(kwargs)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        '''
        Object name setter
        Set name
        '''
        if not value:
            raise ValueError("Name must be defined")
        self.__name=value

    #pseudo-data setter, data attribute inherited
    '''
        Object dictionary setter
        Destructive removes current value
    '''
    def set_Data(self, value):
        #Check that value is of type dictionary and replace data with value
        #Otherwise return error.
        try:
            if not value:
                raise ValueError("Value must be defined")

            if not isinstance(value, dict):
                raise TypeError
            self.clear()
            self.update(value)
        except TypeError as te:
            print("Expected a List got a ", type(value))

    def __add__(self, other):
        '''
        Implementation of '+' operation uses first dictionary and appends data to it.
        Keeps the first dictionarys name
        example:
        If a.name='Dune' and b.name=Neuromancer
        (a+b).name='Dune'
        (a+b).data={Dune dictionary, Neuromancer dictionary}
        If a word in a and b are the same the value in b will clobber the value in a
        '''
        #Current dictionary initialization
        #check the internal data should be type list, other should be type dictionary

        if not other:
            raise ValueError("Other dictionary "+\
                             " must be defined")
        elif not isinstance(other, FictionDict):
            raise TypeError("Other value "+\
                             " must be a FictionDictionary")

        cDict=FictionDict(self.name, self.data)
        cDict.update(other)
        return cDict 

    def __sub__(self, other):
        '''
        Implementation of '-' operation deletes elements of the second dictionary from the first
        Keeps the first dicionarys name
        example
        If a.name='Dune' and b.name=Neuromancer
        (a-b).name='Dune'
        if b is a subset of a then a-b returns a
        Does not delete b.item from a if only b.key== a.key
        Only deletes b.item if b.key==a.key && a.val == b.vall
        Returns the dictionary without the deleted elements
        '''
        #current dictionary initialization
        if not other:
            raise ValueError("Other dictionary "+\
                             " must be defined")
        elif not isinstance(other, FictionDict):
            raise TypeError("Other value "+\
                             " must be a FictionDictionary")

        cDict=FictionDict(self.name, self.data)
        for word, definition in other.items():
            if  word in cDict:
                if other[word] ==cDict[word]:
                    print('Deleting', word)
                    del cDict[word]
                else:
                    print(word, " id not defined like'", word)
            else:
                print(word, "not in", cDict.name)
        return cDict

    def __repr__(self): 
        '''
        Official string repersentation
        For  programatic use. Displays the type, and all attributes of a Fiction Dictionary
        '''
        return 'FictionDict('+self.name+': '+self.data.__repr__()+')'


    def __str__(self):
        '''
        Informal String repersentation
        Implementation of the print method
        Makes print of fiction dictionary, by adding line feeds to each word
        Also adds tab between word and definition
        :return:
        '''
        buildstring=''
        for word in self.data:
            tmpStr=self.wordToString(word)
            buildstring=buildstring+tmpStr
        return buildstring

    def wordToString(self, word):
        '''
        Method to get the string repersentation
        of a word and its definition
        :param word:
        :return: string containing word and definition
        '''

        try:
            if not word:
                raise ValueError("Word can not be empty, must be defined.")
            elif not isinstance(word, str):
                raise TypeError("Word must be a String")
            wordDefs=self.data[word]
            buildString='{0}:'.format(word)
            index=0
            for i in wordDefs:
                if  not index == 0:
                    for i in word:
                        buildstring=buildstring+' '
                buildString=buildString+'\t{0}\n'.format(i)
            return buildString
        except TypeError as te:
            print('Expected string recieved a {0}'.format(type(word)))
        except KeyError as ke:
            print('{0} was not found in  this dictionary.'.format(word))

    def isDuplicateWord(self, word):
        '''
        Checks for duplicate words
         '''
        #Throwing raise outside of the try except allows it to be passed to other functions
        try:
            if not word:
                raise ValueError("Word must be defined")
            elif  not isinstance(word, str):
                raise  TypeError("Word must be a String")
            for w in self.keys():
                if w == word:
                    raise DuplicateWord(word)
                    return True
            return False
        except TypeError as te:
            print('Expected string recieved a {0}'.format(type(word)))
        except DuplicateWord as de:
            print(de.message)
            raise DuplicateWord(word)

    def addWord(self, word):
        '''
        Adds a single word, or dictionary of words to the fiction dictionary.
        '''
        try:
            if not word:
                raise ValueError("Word must be defined")
            elif not isinstance(word, dict):
                raise TypeError("Word must be a String")
        except TypeError as err1:
            print('Expected Dictionary recieved a', type(word))        
        try:
            tempWord=dict()
            for key, val in word.items():
                if self.isDuplicateWord(key):
                    raise DuplicateWord("Word already found in dictionary")
                    return None
                tempWord[key]=val
                self.update(tempWord)      
        except DuplicateWord as err2:
            print(err2.message)

    def editWord(self, word, newDefinition, i=0):
        '''
        Searches for word by word Key and changes the i definition to newDefinition
        If definition not in definition list add it to end of word.
        '''
        try:
            if not word or newDefinition:
                nullValue=("word", "newDefinition")[ word is None]
                raise ValueError(nullValue+ "must be defined")
            elif not isinstance(word, str):
                raise TypeError("Word must be a String")
            elif not isinstance(newDefinition, str):
                raise TypeError("Word must be a String")
            elif  word in self.keys():
                if i < len(self.data[word]):
                    self.data[word][i]=newDefinition
                else:
                    self.data[word].append(newDefinition)
            else:
                raise KeyError
        except TypeError as te:
            print('Expected String recieved a', type(word))
        except KeyError as wnfe:
            print('{0} was not found in the dictionary please add word before modifying'.format(word))
            raise KeyError

    def deleteWord(self, word):
        '''
        Search for word by Key removes the key from fhe dictionary.
        Automatic  Trash collection should take care of the rest
        '''
        try:
            if not isinstance(word, str):
                raise TypeError("Word must be a String.")
            self.pop(word)
        except TypeError as te:
            print('Expected String recieved a', type(word))
        except KeyError as wnfe:
            print('{0} was not found in the dictionary please add word before modifying'.format(word) )
            raise KeyError

    def copyDict(self):
        '''
        Creates a new fiction dictionary with the same data as the current deep copy
        '''
        copyDict=FictionDict(self.name,{})
        for k, i in self.items():
            tempDict={k: []}
            for d in i:
                tempDict[k].append(d)
            copyDict.addWord(tempDict)
        return copyDict

    def buildWordFilter(self):
        '''
        Function creates a iterative filter which is used to parse the dictionary for
        matches
        '''
        pass

    def buildSearchHits(self):
        '''
        Uses the filter returned by build word filter to make a list of matching
        dictionary words
        '''
        pass
