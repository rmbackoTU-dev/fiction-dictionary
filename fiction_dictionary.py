import json, sys, os
from collections import UserDict, defaultdict
from fictDictErr import DuplicateWord
import time

#TODO
#Fix __Str__ to interate through definition list as well as word dictionary
#Redefine set data to use list in data
#Redefine add to use list in data
#Redefine sub to use list in data
#Create Exception class 
# Include DuplicateWord, and WordNotFound
#Create edit Definition
#Check on Copy
#Create tab complete function
#Create export to JSON
#Create inport from JSON

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
        for word, definitions in self.items():
            buildstring=buildstring+word+':\t'
            for d in definitions:
                buildstring=buildstring+d+'\n'
        return buildstring


    def isDuplicateWord(self, word):
        '''
        Checks for duplicate words
        '''
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

    def addWord(self, word):
        '''
        Adds a single word, or dictionary of words to the fiction dictionary.
        '''
        try:
            if not isinstance(word, dict):
                raise TypeError
        except TypeError as err1:
            print('Expected Dictionary recieved a', type(word))        
        try:
            if self.isDuplicateWord(word):
                return
            self.update(word)
        except DuplicateWord as err2:
            print(err2.message)

    def editWord(self, word, newDefinition, i=0):
        '''
        Searches for word by word Key and changes the i definition to newDefinition
        If definition not in definition list add it to end of word.
        '''
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

    def deleteWord(self, word):
        '''
        Search for word by Key removes the key from fhe dictionary. 
        Automatic  Trash collection should take care of the rest
        '''
        try:
            if not isinstance(word, str):
                raise TypeError
            self.pop(word)
        except TypeError as te:
            print('Expected String recieved a', type(word))
        except KeyError as wnfe:
            print('{0} was not found in the dictionary please add word before modifying'.format(word) )
            raise KeyError

    def importJSON(self, dictName, filename):
        '''
        Import a diction object from a JSON so it can be shared, and edited by the native application
        Takes file name as absolute path in case file is not saved in dictionary directory
        '''
        try:
            with open(filename, 'r+') as json_file:
                importDict=json.load(json_file)
                importFictDict=FictionDict(dictName, importDict)
                json_file.close()
                return importFictDict
        except FileNotFoundError as fnfe:
            print('There is no file found by the name {0}'.format(filename))


    def exportJSON(self, filename=''):
        '''
        Write dictionary objct to a JSON file so it can be saved and used by other applications
        Overwrites any previous json files by the same name. Write to the dictionaries directory
        Use the Eastern timezone unless otherwise specified
        '''
    
        timeStr=time.strftime('%Y%B%d')
        dict_dir=os.path.dirname(os.path.realpath(__file__))+'/dictionaries/'
        if  filename == '':
            #the default filename should have the name of the dictionary YearMonthDay
            filename="{0}{1}-{2}.json".format(dict_dir, self.name,timeStr)
        else:
            filename=dict_dir+filename+'.json'
        with open(filename, 'w' ) as json_file:
            json.dump(self.data, json_file)
            json_file.close()

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
        pass

         