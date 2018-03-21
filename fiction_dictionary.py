import json, sys
from collections import UserDict, defaultdict
#TODO:
#Implement against test features.
class FictionDict(UserDict):
    '''
    Fiction Dictionary Class: inherits from UserDict dict wrapper
    Description: used to create fiction dictionaries which can be saved to exported from json files
    '''

    #Keep class generation generic do the fancy stuff later
    def __init__(self, name="",  data=defaultdict(lambda: "Not defined yet"), **kwargs):
        UserDict.__init__(self)
        self.name=name
        self.update(data)
        self.update(kwargs)

    @property
    def name(self):
        '''{
        Object name getter
        '''
        return self.__name

    @name.setter
    def name(self, value):
        '''
        Object name setter
        Set name
        Todo: Implement checking
        '''
        self.__name=value
    
    #pseudo-data setter, data attribute inherited
    def set_Data(self, value):
        '''
        Object dictionary setter
        Destructive removes current value
        '''
        #Check that value is of type dictionary and replace data with value
        #Otherwise return error.
        try:
            if isinstance(value, dict):
                self.clear()
                self.update(value)
            else:
                raise TypeError
        except TypeError as te:
            print("Expected a Dictionary got a ", type(value))




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
        Informal string repersentation
        Implementation of the print method.
        Makes print of fiction Dictionary, by adding line feeds to each word
        Also adds tab between word and definition
        '''
        buildstring=''
        for word, definition in self.items():
            buildstring=buildstring+word+':\t'+definition+'\n'
        return buildstring


    def addWord(self, wordDict):
        '''
        Adds a single word, or dictionary of words to the fiction dictionary.
        '''
        self.data.update(wordDict)

