import os, sys, datetime
from pathlib import Path
import json


#TODO
'''
For a list of dictionaries first check if the dictionary exist in the list before setting it
'''

class dataFile():
    #directory does not get to be choose by use
    topLevelDir=Path(os.path.dirname(os.path.abspath(__file__))).parent

    #context is the current dictionary that the program is writing to 
    def __init__(self):
        self.temp_file='temp.json'
        self.temp_abs=os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
        self.currentContext={}
        self.dict_collection={}
        
    def setFileName(self, filename):
       self.temp_file=filename
       self.temp_abs=os.path.join(self.topLevelDir, 'dictionaries', self.temp_file)
    
    #This sould only be done initially. it will overwrite the current context
    def  setNewDictionary(self, dict_of_list, dictName):
        self.dict_collection[dictName]=dict_of_list
        self.currentContext=dict_of_list

    #Update file dumps the current dictionary the user is writing to a temp file
    def updateFile(self):
       pass

    #delete file deletes the current temp file, may attempt to call this after some condition automatically
    def  deleteFile(self):
        pass

    #create file creates a new temp file if one does not exist, assigns the context dictionary
    # to the file
    #if one exist set the context to the first item
    #Always should return a dictionary : including current context and Error passed if any
    def createFile(self):
        data_list={"currentContext": self.currentContext}
        try:
            if os.path.isfile(self.temp_abs):
                with open(self.temp_abs, 'r') as f:
                    data_list=json.load(f)
                    #Get the first dictionary off the list and set it as the context if the file exist
                    self.currentContext=next(iter(data_list.values()))
                    return data_list
            else:
            	raise(FileNotFoundError)
        except (FileNotFoundError, IOError): 
            print(": Creating a new temp file: ")
            try:
                if  data_list["currentContext"]:
                    with open(self.temp_abs, 'a+') as f:
                        json.dump(data_list, f)
                        return data_list
                else:
                	raise(ValueError)
            except ValueError:
            	valErr="No default dictionary context was set create a populated dictionary first"
            	data_list["Error0"]=valErr
            	print(data_list["Error0"])
            	return data_list

    
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




