import json, os
from fiction_dictionary import FictionDict


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
        if(pid == None):
            raise ValueError("The process id must be set")

        self.pid=pid

        if(pathname == None):
            raise ValueError("The pathname must be set")
        self.file=pathname

    def exportJSON(self, data):
        try:
            print('{0} writing to {1}'.format((self.pid, self.pathname)))
            with open(self.pathname, 'a+' ) as json_file:
                json.dump(data, json_file)
                json_file.close()
        except IOError as ioe:
            print('An error occured while opening {0} to write'.format(self.pathname))

    def exportOverwriteJSON(self, data):
        try:
            print('{0} overwriting to {1}'.format((self.pid, self.pathname)))
            with open(self.pathname, 'w') as json_file:
                json_file.seek(0)
                json.dump(data, json_file)
                json_file.truncate()
        except IOError as ioe:
            print("An error occured while opening {0} to overwrite".format(self.pathname))

    def importJSON(self):
        try:
            print('{0} reading from {1}'.format(self.pid, self.pathname))
            with open(self.pathname, 'r+') as json_file:
                importData: FictionDict=json.load(json_file)
                json_file.close()
            return importData
        except:
            print('An error occured while opening {0}'.format(self.pathname))

    def deleteJSON(self):
        try:
            os.remove(self.pathname)
            print("{0} deleted by process {1} ".format(self.pathname, self.pid))
        except:
            print('An error occured while deleting {0}'.format(self.pathname))


