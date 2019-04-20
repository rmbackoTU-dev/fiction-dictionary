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
        #Todo: Implement checking
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
            if not isinstance(value, dict):
                raise TypeError
            self.clear()
            self.update(value)
        except TypeError as te:
            print("Expected a List got a ", type(value))

    '''
        Implementation of '+' operation uses first dictionary and appends data to it.
        Keeps the first dictionarys name
        example:
        If a.name='Dune' and b.name=Neuromancer
        (a+b).name='Dune'
        (a+b).data={Dune dictionary, Neuromancer dictionary}
        If a word in a and b are the same the value in b will clobber the value in a
    '''
    def __add__(self, other):
        #Current dictionary initialization
        #check the internal data should be type list, other should be type dictionary
        cDict=FictionDict(self.name, self.data)
        cDict.update(other)
        return cDict 

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
    def __sub__(self, other):
        #current dictionary initialization
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

        '''
        Informal string repersentation
        Implementation of the print method.
        Makes print of fiction Dictionary, by adding line feeds to each word
        Also adds tab between word and definition
        '''
    def __str__(self):
        buildstring=''
        for word in self.data:
            tmpStr=self.wordToString(word)
            buildstring=buildstring+tmpStr
        return buildstring

    def wordToString(self, word):
        try:
            if not isinstance(word, str):
                raise TypeError
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

    '''
        Checks for duplicate words
    '''
    def isDuplicateWord(self, word):
        #Throwing raise outside of the try except allows it to be passed to other functions
        try:
            if  not isinstance(word, str):
                raise  TypeError
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

    '''
        Adds a single word, or dictionary of words to the fiction dictionary.
    '''
    def addWord(self, word):
        try:
            if not isinstance(word, dict):
                raise TypeError
        except TypeError as err1:
            print('Expected Dictionary recieved a', type(word))        
        try:
            tempWord=dict()
            for key, val in word.items():
                if self.isDuplicateWord(key):
                    raise DuplicateWord
                    return None
                tempWord[key]=val
                self.update(tempWord)      
        except DuplicateWord as err2:
            print(err2.message)

    '''
        Searches for word by word Key and changes the i definition to newDefinition
        If definition not in definition list add it to end of word.
    '''
    def editWord(self, word, newDefinition, i=0):
        try:
            if not isinstance(word, str):
                raise TypeError
            elif not isinstance(newDefinition, str):
                raise TypeError
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
    '''
        Search for word by Key removes the key from fhe dictionary. 
        Automatic  Trash collection should take care of the rest
    '''
    def deleteWord(self, word):
        try:
            if not isinstance(word, str):
                raise TypeError
            self.pop(word)
        except TypeError as te:
            print('Expected String recieved a', type(word))
        except KeyError as wnfe:
            print('{0} was not found in the dictionary please add word before modifying'.format(word) )
            raise KeyError

    '''
        Write dictionary objct to a JSON file so it can be saved and used by other applications
        Overwrites any previous json files by the same name. Write to the dictionaries directory
        Use the Eastern timezone unless otherwise specified

        Change: Added dict_dir to function so it could be specified at top level directory
    '''
    def exportJSON(self, dict_dir, filename=''):
        timeStr=time.strftime('%Y%B%d')
        if  filename == '':
            #the default filename should have the name of the dictionary YearMonthDay
            filename="{0}{1}-{2}.json".format(dict_dir, self.name,timeStr)
        else:
            filename=dict_dir+filename+'.json'
        with open(filename, 'w' ) as json_file:
            json.dump(self.data, json_file)
            json_file.close()

    '''
        Creates a new fiction dictionary with the same data as the current deep copy
    '''
    def copyDict(self):
        copyDict=FictionDict(self.name,{})
        for k, i in self.items():
            tempDict={k: []}
            for d in i:
                tempDict[k].append(d)
            copyDict.addWord(tempDict)
        return copyDict

    '''
        Function creates a iterative filter which is used to parse the dictionary for
        matches
    '''
    def buildWordFilter(self):
        pass

    '''
        Uses the filter returned by build word filter to make a list of matching
        dictionary words
    '''
    def buildSearchHits(self):
        pass
