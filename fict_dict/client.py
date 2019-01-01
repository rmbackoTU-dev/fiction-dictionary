import sys, os, argparse, json, datetime
from fiction_dictionary import FictionDict
from exceptions import DuplicateWord
'''
Interface class makes fiction dictionary classes callable by different modes and unit test
'''
class CommandLineLib():
     
	#class variables:
    fDict=[]
    fDictCount=0
    fDictCurrent=0
    cacheDir='/FictionDictCache'

    def __init__(self, dicDir=''):
        self. dictionaryDirectory=dicDir

    @property
    def fDictCurrentDict(self):
    	return fDict[fDictCurrent] 

    @property
    def dictionaryDirectory(self):
    	return self._dictionaryDirectory
    
    @dictionaryDirectory.setter
    def dictionaryDirectory(self, dicDir):
    	'''
		TODO:
		Add error checking to  make sure location exist
    	'''
    	self.__dictionaryDirectory=dicDir

    def create(self, name):
        fDict[fDictCount]=[FictionDict(name, {})]
        fDictCount+=1

    def select(self, num):
	    fDictCurrent=num

    def remove(self, word):
	    self.fDictCurrentDict.deleteWord(word)

    def delete(self):
        curr=fDictCurrent
        while fDict[curr+1] != None:
            print(curr)
            print(fDict[curr].name())
            fDict[curr]=curr+1

    def addWord(self, word, definitions):
	    wordDict={word:[]}
	    for i in definitions:
		    wordDict[0].append(i)
	        #fDict[fDictCurrenti].addWord(wordDict)

    def editWord(self, word, definition, defNum=0):
	    fDictCurrentDict.editWord(word, definition, defNum)

    def listDicts(self):
	    for i, d in fDict:
		    print('{0}: \t {1}'.format(i, d.name()))

    def save(self, filename=''):
	    if filename =='':
		    filename=self.fictDict.name
	    completeFN=self.dictionaryDirectory+filename
	    fDictCurrentDict.exportJSON(filename)

    def printDict(self):
	    print(fDictCurrent)

    def printWord(self, word):
	    printStr=fDictCurrentDict.wordToString(word)
	    print(printStr)

    def dictionaryAdd(self, secondDictNum):
        newDict=fDictCurrentDict + fDict[secondDictNume]
        decision='Err'
        while decision != 'New' or decision != 'Current':
            desicion=input('Would you like to add to your current dictionary or add a new dictionary with the result? (New/Current)')
            if decision == 'Current':
                fDictCurrentDict=newDict
            elif decision == 'New':
                fDict.append(newDict)

    def dictDiff(self, secondDictNum, storeDifference=False):
	    differenceDict=fDictCurrentDict-fDict[secondDictNum]
	    if storeDifference:
		    fDict.append(dictionaryDirectory)
	    else:
		    print(differenceDict)

    def importJSON(self, dictName, filename):
        '''
        Import a diction object from a JSON so it can be shared, and edited by the native application
        Takes file name as absolute path in case file is not saved in dictionary directory
         Better suited as menu item since importing a JSON should not depend on an existing dictionary
        Since there is no existing dictionary
        '''
        try:
            with open(filename, 'r+') as json_file:
                importDict=json.load(json_file)
                importFictDict=FictionDict(dictName, importDict)
                json_file.close()
                fDict.append(importFictDict)
        except FileNotFoundError as fnfe:
            print('There is no file found by the name {0}'.format(filename))
        useAsCurrent='Err'
        while useAsCurrent != 'Y' and useAsCurrent !='N':
            useAsCurrent=input("Would you like to use your imported dictionary as your current dictionary? (Y/N)")
            if useAsCurrent == "Y":
        	    fDictCurrent=len(fDict)
        
    def createDictionaryCache(self, index):
        #Simplest way to store definitions in-between sessions
        try:
            if not os.path.isdir(sys.path.append(os.path.dirname(__file__), cacheDir)):
                os.mkdir(cache, 644)
            else:
                theDate=datetime.date()
                cacheFileName="fdictCache_"+theDate.today().__str__()+index.__str__
                #Create a cache file with the current date do not write
                os.open(cacheFileName, 'a').close()
        except OSError:
            print("Creation of the  cache directory %s failed", cacheDir)


    def updateCache(self, index):
        #update current cache, with the dictionary at the given index

    def cleanOldCache(self, mtime):
        #clean cache files based on modify time of  mtime

