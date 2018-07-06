class WordNotFoundErr(Exception):
    '''Raised when the data input can not find a corresponding key (word)'''
    def  __init__(self, word, message=None):
        if not message:
            self.message='{0} was not found in the dictionary please add word before modifying'.format(word) 
        else:
            self.message=message

    @property
    def message(self):
    	return self._message
    
    def message(self, value):
    	self.__message=value

class DuplicateWord(Exception):
    '''Raised when a key (word) entry is already present in the dictionary'''
    def __init__(self, word, message=None):
        if not message:
            self.message='{0} was already found in the dictionary, please modify the current entry'.format(word)
        else:
        	self.message=message

    @property
    def message(self):
    	return self._message
    
    def message(self, value):
    	self.__message=value
