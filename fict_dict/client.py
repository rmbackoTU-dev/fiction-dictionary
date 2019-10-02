import os
from fict_dict.fiction_dictionary import FictionDict
from fict_dict.dataFile import dataFile

'''
Client class used to call use functionality of fiction dictionary
'''

class fict_dict_cli_access():

    def __init__(self):
        pid=os.getpid()


    def createDictionary(self, dictName, fileName):
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

    def get_word_Str(self, srcFile, word):
        targetDictionary=dataFile(self.pid, srcFile)
        importDict: FictionDict=targetDictionary.importJSON()
        wordStr=importDict.wordToString(word)
        return wordStr

    def get_dict_Str(self, srcFile):
        targetDictionary=dataFile(self.pid, srcFile)
        importDict: FictionDict=targetDictionary.importJSON()
        dictStr=importDict.__str__()
        return dictStr

    def searchDict(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid, dictFile )
        matchList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.searchDict(searchWord)
        return matchList

    def searchLeftDict(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid, dictFile)
        matchList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.left_to_right_match_list(searchWord)
        return matchList

    def searchRightDict(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid, dictFile)
        matchList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.right_to_left_match_list(searchWord)
        return matchList

    def searchDictWithDef(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid, dictFile)
        strList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.searchDict(searchWord)
        tempStr=""
        for word in matchList:
            tempStr=importDict.wordToString(word)
            strList.append(tempStr)
        return strList

    def searchDictLeftDict(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid, dictFile)
        strList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.left_to_right_match_list(searchWord)
        for word in matchList:
            tempStr=importDict.wordToString(word)
            strList.append(tempStr)
        return strList

    def searchDictRightDict(self, dictFile, searchWord):
        searchTarget=dataFile(self.pid)
        strList=[]
        importDict: FictionDict=searchTarget.importJSON()
        matchList=importDict.right_to_left_match_list(searchWord)
        for word in matchList:
            tempStr=importDict.wordToString(word)
            strList.append(tempStr)
        return strList