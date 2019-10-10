import json, sys, os
from collections import UserDict, defaultdict
from fict_dict.exceptions import DuplicateWord

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
    def __init__(self, name=" ",  data=dict(), **kwargs):
        UserDict.__init__(self)
        self.name=name
        #check presence of kwargs first
        if not kwargs :
            self.update(data)
        else:
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
        if value is None:
            raise ValueError("Name must be defined")
        self.__name=value

    def set_Data(self, value, **kwargs):
        '''
        Objec dictionary setter
        Destructive removes current value
        data attribute for inherited UserDict
        :param value:
        :param kwargs:
        '''
        #Check that value is of type dictionary and replace data with value
        #Otherwise return error.
        try:
            set=(kwargs is None)
            if  not kwargs:
                #check value if empty throw error
                if value is None:
                    raise ValueError("Value must be defined")
                if not isinstance(value, dict):
                    raise TypeError
                else:
                    self.clear()
                    self.update(value)
            #kwargs is a dictionary by default and does not need a typeCheck
            else:
                self.clear()
                self.update(kwargs)
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
        if not other :
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
                    print(word, " id not defined like ", word)
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
        :param word: a Dictionary maping a string/tuples to a list of strings
        :return: string containing word and definition
        '''

        try:
            if not word:
                raise ValueError("Word can not be empty, must be defined.")
            elif not isinstance(word, str):
                raise TypeError("Word must be a Dictionary")
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
        if not word:
            raise ValueError("Word must be defined")
        elif not isinstance(word, str):
            error='Expected string recieved a {0} '.format(type(word))
            raise TypeError(error)
        for w in self.keys():
            if w == word:
                #raise DuplicateWord(word)
                return True
        return False
        #except DuplicateWord as de:
            #print(de.message)
            #raise DuplicateWord(word)

    def addWord(self, word):
        '''
        Adds a single word, or dictionary of words to the fiction dictionary.
        '''
        try:
            if word is None:
                raise ValueError("Word must be defined")
            elif not isinstance(word, dict):
                raise TypeError('Expected Dictionary recieved a '.format(type(word)))
            for key in word.keys():
                if self.isDuplicateWord(key):
                    raise DuplicateWord("Word already found in dictionary")
                    return None
                self.update(word)
        except DuplicateWord as err2:
            print(err2.message)

    def editWord(self, word, newDefinition, i=0):
        '''
        Retrieves word by Key and changes the i definition to newDefinition
        If definition not in definition list add it to end of word.
        '''
        try:
            if word is None or newDefinition is None:
                nullvalue="newDefinition" if [word is None] else "word"
                raise ValueError(nullvalue+ " must be defined")
            elif not isinstance(word, str):
                raise TypeError("Word must be a String")
            elif not isinstance(newDefinition, str):
                raise TypeError("New Definition must be a String")
            elif word in self.keys():
                if i < len(self.data[word]):
                    self.data[word][i]=newDefinition
                else:
                    self.data[word].append(newDefinition)
            else:
                raise KeyError
        except KeyError as wnfe:
            error='{0} was not found in the dictionary please add word before modifying'.format(word)
            raise KeyError(error)

    def deleteWord(self, word):
        '''
        Search for word by Key removes the key from fhe dictionary.
        Automatic  Trash collection should take care of the rest
        '''
        try:
            if not isinstance(word, str):
                raise TypeError('Expected String recieved a '.format(type(word)))
            del self.data[word]
        except KeyError as wnfe:
            error='{0} was not found in the dictionary please add word before modifying'.format(word)
            raise KeyError(error)

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

    def searchDict(self, substring):
        '''
        searches Dict for substring in
        each dict key and returns list of closest matching
        words (keys)
        :param: expression
        :return: left to right and right to left list of matches
        '''
        if substring is None:
            raise ValueError("Substring must be defined")
        elif not isinstance(substring, str):
            raise TypeError("SubString must be a string")
        left_to_right_list=self.left_to_right_match_list(substring)
        right_to_left_list=self.right_to_left_match_list(substring)
        full_match_list=left_to_right_list.append(right_to_left_list)
        return full_match_list

    def left_to_right_match_list(self, search_string):
        '''
        match string to keys from left to right
        :param string:
        :return:  List of keys in dict containing string as sub string
        '''
        if not search_string:
            raise ValueError("Substring must be defined")
        elif not isinstance(search_string, str):
            raise TypeError("SubString must be a string")
        matchs=[]
        search_string_len=len(search_string)
        for k in self.keys():
            #i is a character position for k
            i=0
            keyString_len=len(k)
            str_len_difference=keyString_len-search_string_len
            '''
            The length must not exceed the amount
            that would allow the entire search string to be found
            '''
            while i <=str_len_difference and not matchs.__contains__(k):
                #j is a character position for search_string
                j=0
                current_char=i+j
                while (j < search_string_len and k[current_char]== search_string[j]):
                    j=j+1
                    current_char=i+j
                if j>= search_string_len:
                    #instead of returning the subString consider key a match
                    matchs.append(k)
                i=i+1
            #instead of returning non-indexable value move to next word
        return matchs


    def right_to_left_match_list(self, search_string):
        '''
        match string to keys from right to left
        :param string:
        :return: List of keys in dict containing string as sub String
        '''
        if not search_string:
            raise ValueError("Substring must be defined")
        elif not isinstance(search_string, str):
            raise TypeError("SubString must be a string")
        matchs=[]
        search_string_len=len(search_string)
        for k in self.keys():
            #i is a character position for k
            i=0
            key_len=len(k)
            string_len_diff=key_len-search_string_len
            '''
            The length must not exceed the amount
            that would allow the entire search string to be found
            '''
            while i < string_len_diff and  not matchs.__contains__(k):
                #j is a character position for search string
                #in right to left it is the last position
                j=search_string_len-1
                '''
                compares keeps track of the characters in the search string
                 to compare while j keeps track of the position
                 this is essential so matches left can be tracked  without effecting
                array index
                '''
                compares=search_string_len
                current_char=i+j
                while( j >0 and k[current_char]== search_string[j]):
                    j=j-1
                    compares=compares-1
                    current_char=i+j
                if compares == 0:
                    #instead of returning the subString consider key a match
                    matchs.append(k)
                i=i+1
            #instead of returning non-indexable value move to next word
        return matchs
