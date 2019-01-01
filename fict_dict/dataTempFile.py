import os, sys, datetime
import json

class dataTempFile :

	localCacheDir=os.path.dirname(os.path.abspath(__file__))

	def __init__():
		self.temp_file='temp'
		self.tempDir='/temp'
        self.temp_abs=os.path.join(localCacheDir, tempDir, temp_file)

	def __init__(filename, dirName):
       self.temp_file=filename
       self.tempDir=dirName
       self.temp_abs=os.path.join(localCacheDir, tempDirm temp_file)

	def updateFile(dictionary):
		pass

	def  deleteFile():
		pass

	def createFile():
		pass

	def readKey():
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




