import sys, os, argparse, json, datetime
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.exceptions import DuplicateWord
from fict_dict.dataFile import dataFile

'''
Client class used to call use functionality of fiction dictionary
'''

class fictDictClient():
    '''
    todo:
    create a dictionary
    delete a dictionary
    edit a dictionary
    add two dictionaries
    get the difference between two dictionaries
    search a single dictionary
    copy a dictionary to a new file
    '''

	#class variables:
    cacheDir='/FictionDictCache'


    def __init__(self):
        pid=os.getpid()


    def createDictionaryName(self, dictName, fileName):
        newDict=FictionDict(dictName)
        newDataFile=dataFile(self.pid, fileName)
        newDataFile.exportJSON(newDict)

    def deleteDictionary(self, fileName):
        '''
        Delete a dictionary file from the system
        :param fileName
        '''
        newDataFile=dataFile(self.pid, fileName)
        newDataFile.deleteJSON()

    def editDictionary(self, fileName, word, definition, synonm):
        newDataFile=dataFile(self.pid, fileName)
        importedDictionary: FictionDict=newDataFile.importJSON()
        importedDictionary.editWord(word,definition, synonm)
        newDataFile.exportOverwriteJSON(importedDictionary)


    def addDictionaries(self, fileNameOne, fileNameTwo):
        newDataFileOne=dataFile(self.pid, fileNameOne)
        newDataFileTwo=dataFile(self.pid, fileNameTwo)
        importDictionaryOne: FictionDict=newDataFileOne.importJSON()
        importDictionaryTwo: FictionDict=newDataFileTwo.importJSON()
        sumDict=importDictionaryOne+importDictionaryTwo
        newDataFileOne.exportOverwriteJSON(sumDict)

    def diffDictionaries(self, fileNameOne, fileNameTwo):
        newDataFileOne=dataFile(self.pid, fileNameOne)
        newDataFileTwo=dataFile(self.pid, fileNameTwo)
        importDictionaryOne: FictionDict=newDataFileOne.importJSON()
        importDictionaryTwo: FictionDict=newDataFileTwo.importJSON()
        diffDict=importDictionaryOne-importDictionaryTwo
        newDataFileOne.exportOverwriteJSON(diffDict)

    def copyDictionaries(self, srcFile, destFile):
        oldDataFile=dataFile(self.pid, srcFile)
        newDataFile=dataFile(self.pid, destFile)
        importDict: FictionDict=oldDataFile.importJSON()
        exportDict=importDict.copyDict()
        newDataFile.exportJSON(exportDict)




