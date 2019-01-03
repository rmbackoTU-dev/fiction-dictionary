import os, sys, datetime
import json

class dataTempFile :
    
    #directory does not get to be choose by user
	self.localCacheDir=os.path.dirname(os.path.abspath(__file__))

    #context is the current dictionary that the program is writing to 
	def __init__(self):
		self.temp_file='temp'
        self.temp_abs=os.path.join(localCacheDir, 'temp', temp_file)
        self.currentContext={}

	def __init__(self, filename):
       self.temp_file=filename
       self.temp_abs=os.path.join(localCacheDir, 'temp', temp_file)
       self.currentContext={}
    
    def  __init__(self, filename, dictionary):
        self.temp_file=filename
        self.temp_abs=os.path.join(localCacheDir, 'temp', temp_file)
        self.currentContext=dictionary

    #Update file dumps the current dictionary the user is writing to a temp file
	def updateFile(self):
		pass

    #delete file deletes the current temp file, may attempt to call this after some condition automatically
	def  deleteFile(self):
		pass

    #create file creates a new temp file if one does not exist already
	def createFile(self):
		pass
    
    #print dictionary at  outputs the file to a dictionary and reads in the dictionary pointed to by the key
	def printDictionaryAt(self, key):
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




