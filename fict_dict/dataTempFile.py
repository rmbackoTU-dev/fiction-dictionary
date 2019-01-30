import os, sys, datetime
from pathlib import Path
import json
from collections import ChainMap

#TODO
'''
Implement Functions
'''

class dataFile():
    #directory does not get to be choose by user
    topLevelDir=Path(os.path.dirname(os.path.abspath(__file__))).parent

    #context is the current dictionary that the program is writing to 
    def __init__(self):
        self.temp_file='temp.json'
        self.temp_abs=os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
        self.currentContext={}

    def setFileName(self, filename):
       self.temp_file=filename
       self.temp_abs=os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
    
    #This sould only be done initially. it will overwrite the current context
    def  setNewDictionary(self,  dictionary):
        self.currentContext=dictionary

    #Update file dumps the current dictionary the user is writing to a temp file
    def updateFile(self):
       pass

    #delete file deletes the current temp file, may attempt to call this after some condition automatically
    def  deleteFile(self):
        pass

    #create file creates a new temp file if one does not exist, assigns the context dictionary
    # to the file
    #if one exist set the context to the first item
    def createFile(self):
        data_list={1: self.currentContext}
        try:
            if os.path.isfile(self.temp_abs):
                with open(self.temp_abs, 'r') as f:
                    data_list=json.load(f)
                    #Get the first dictionary off the list and set it as the context if the file exist
                    self.currentContext=next(iter(data_list.values()))
                    return self.currentContext
            else:
            	raise(FileNotFoundError)
        except (FileNotFoundError, IOError): 
            print(": Creating a new temp file: ")
            try:
                if  data_list[1]:
                    with open(self.temp_abs, 'a+') as f:
                        json.dump(data_list, f)
                        return self.currentContext
                else:
                	raise(ValueError)
            except ValueError:
            	print("No default dictionary context was set create a populated dictionary first")
            	return { 0 :["No default dictionary context was set create a populated dictionary first"]}

    
    #print dictionary which is pointed to by key
    def printCurrent(self, key):
        pass

    #set Context sets the current diectionary to the dictionary pointed to by the key
    def setContext(self, key):
        pass

    #Check to see if file contains a key
    def __contains__(key):
        try:
            found=False
            fileDict={}
            if not os.file.exists(temp_abs):
                return found;
            else:
                with os.open(temp_abs, 'r') as temp:
                    fileDict=json.load(temp_abs)
                    for k in fileDict.keys():
                        if(k == key):
                            found=True
                    temp.close()
                return found
        except:
            print("Error while reading temporary file")
            return found




