import sys, os, argparse, json, datetime
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.exceptions import DuplicateWord
'''
Interface class makes fiction dictionary classes callable by different modes and unit test
'''


class CommandLineLib:
     
    #class variables:
    fDict = []
    fDictCount = 0
    fDictCurrent = 0
    cacheDir = '/FictionDictCache'

    def __init__(self, dicDir = ''):
        self. dictionaryDirectory = dicDir

    @property
    def fDictCurrentDict(self):
        return self.fDict[self.fDictCurrent]

    @property
    def dictionaryDirectory(self):
        return self._dictionaryDirectory
    
    @dictionaryDirectory.setter
    def dictionaryDirectory(self, dicDir):
        #TODO:
        #Add error checking to  make sure location exist
        self.__dictionaryDirectory = dicDir

    def create(self, name):
        self.fDict[self.fDictCount] = [FictionDict(name, {})]
        self.fDictCount += 1

    def select(self, num):
        self.fDictCurrent = num

    def remove(self, word):
        self.fDictCurrentDict.deleteWord(word)

    def delete(self):
        curr = self.fDictCurrent
        while self.fDict[curr+1] is not None:
            print(curr)
            print(self.fDict[curr].name())
            self.fDict[curr]=curr+1

    def add_word(self, word, definitions):
        wordDict={word:[]}
        for i in definitions:
            wordDict[0].append(i)
            #fDict[fDictCurrent].addWord(wordDict)

    def edit_word(self, word, definition, defNum=0):
        self.fDictCurrentDict.edit_word(word, definition, defNum)

    def list_dictionaries(self):
        for i, d in fDict:
            print('{0}: \t {1}'.format(i, d.name()))

    def save(self, filename=''):
        if filename == '':
            filename = self.fictDict.name
        completeFN = self.dictionaryDirectory+filename
        self.fDictCurrentDict.exportJSON(filename)

    def printDict(self):
        print(self.fDictCurrent)

    def printWord(self, word):
        printStr = self.fDictCurrentDict.wordToString(word)
        print(printStr)

    def dictionary_add(self, secondDictNum):
        new_dict = self.fDictCurrentDict + self.fDict[secondDictNum]
        decision = 'Err'
        while decision != 'New' or decision != 'Current':
            decision = input('Would you like to add to your current dictionary or \
                add a new dictionary with the result? (New/Current)')
            if decision == 'Current':
                f_dict_current_dict = new_dict
            elif decision == 'New':
                self.fDict.append(new_dict)

    def dictDiff(self, secondDictNum, storeDifference=False):
        differenceDict=self.fDictCurrentDict-self.fDict[secondDictNum]
        if storeDifference:
            self.fDict.append(self.dictionaryDirectory)
        else:
            print(differenceDict)

    '''
    Import a diction object from a JSON so it can be shared, and edited by the native application
    Takes file name as absolute path in case file is not saved in dictionary directory
    Better suited as menu item since importing a JSON should not depend on an existing dictionary
    Since there is no existing dictionary
    '''
    def import_JSON(self, dictName, filename):
        try:
            with open(filename, 'r+') as json_file:
                import_dict = json.load(json_file)
                import_fict_dict = FictionDict(dictName, import_dict)
                json_file.close()
                self.fDict.append(import_fict_dict)
        except FileNotFoundError as fnfe:
            print('There is no file found by the name {0}'.format(filename))
        use_as_current = 'Err'
        while use_as_current != 'Y' and use_as_current != 'N':
            use_as_current = input("Would you like to use your imported dictionary  \
                as your current dictionary? (Y/N)")
            if use_as_current == "Y":
                self.fDictCurrent = len(self.fDict)
        




