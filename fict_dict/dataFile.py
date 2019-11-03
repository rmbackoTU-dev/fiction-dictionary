import json, os
from fict_dict.fiction_dictionary import FictionDict

class dataFile():

    '''
    Used to manage multiple files being read and written to by the an application
    '''


    def __init__(self, pid, pathname):
        '''
        Constructor for the dataFile Class
        :param pid: process locking the file
        :param filename: file name of the file being locked by the current application
        '''
        if not pid:
            raise ValueError("The process id must be set")
        self.pid=pid

        if not pathname:
            raise ValueError("The pathname must be set")
        self.file=pathname
        print(self.file)

    def exportJSON(self, data):
        if data is None:
            raise ValueError("Data to be exported has not been set")
        else:
            print('{0} writing to {1}'.format(self.pid, self.file))
            with open(self.file, 'a+' ) as json_file:
                json.dump(data, json_file)
                json_file.close()

    def exportOverwriteJSON(self, data):
        if data is None:
            raise ValueError("Data to be exported has not been set")
        else:
            if not os.path.isfile(self.file):
                raise IOError("This file does not exist.")
            print('{0} overwriting to {1}'.format(self.pid, self.file))
            with open(self.file, 'w') as json_file:
                json_file.seek(0)
                json.dump(data, json_file)
                json_file.truncate()

    def importJSON(self):
        if not os.path.isfile(self.file):
            raise IOError("This file does not exist")
        else:
            print('{0} reading from {1}'.format(self.pid, self.file))
            with open(self.file, 'r+') as json_file:
                importData=json.load(json_file)
                dictName=importData["Name"]
                del (importData["Name"])
                dictData: FictionDict=FictionDict(dictName, importData)
                json_file.close()
            return dictData

    def deleteJSON(self):
        if not os.path.isfile(self.file):
            raise IOError("This file does not exist")
        else:
            os.remove(self.file)
            print("{0} deleted by process {1} ".format(self.file, self.pid))