import os, sys, datetime
import json

#TODO
'''
Implement Functions
'''

class dataFile():
    #directory does not get to be choose by user
    localCacheDir=os.path.dirname(os.path.abspath(__file__))

    #context is the current dictionary that the program is writing to 
    def __init__(self):
        self.temp_file='temp'
        self.temp_abs=os.path.join(self.localCacheDir, 'temp', self.temp_file)
        self.currentContext={}

    def setFileName(self, filename):
       self.temp_file=filename
       self.temp_abs=os.path.join(self.localCacheDir, 'temp', self.temp_file)
    
    #This sould only be done initially. it will overwrite the current context
    def  setNewDictionary(self, filename, dictionary):
        self.currentContext=dictionary

    #Update file dumps the current dictionary the user is writing to a temp file
    def updateFile(self):
       pass

    #delete file deletes the current temp file, may attempt to call this after some condition automatically
    def  deleteFile(self):
        pass

    #create file creates a new temp file if one does not exist already
    def createFile(self):
        try:
            if (os.path.exists(self.temp_abs)):
                return True
            else:
                with open(self.temp_abs, 'a') as f:
                    f.close()
                    return True
        except:
            print("IO Error during file creation")
            return False
    
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




